import streamlit as st
from rag_pipeline import load_pdf, get_chunks, get_vectorstore, get_chain

st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 Context-Aware PDF Chatbot")
st.caption("Powered by GROQ + LangChain + RAG")

# ── Sidebar: Upload PDF ───────────────────────────────────────
with st.sidebar:
    st.header("Upload your PDF")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

    if uploaded_file and st.button("Process PDF"):
        with st.spinner("Reading and indexing PDF..."):
            # Save temporarily
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            raw_text = load_pdf("temp.pdf")
            chunks   = get_chunks(raw_text)
            vs       = get_vectorstore(chunks)
            st.session_state.chain = get_chain(vs)
            st.session_state.chat_history = []
            st.success(f"✅ Indexed {len(chunks)} chunks!")

# ── Chat Interface ────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Ask something about your PDF..."):
    if "chain" not in st.session_state:
        st.warning("⚠️ Please upload and process a PDF first.")
    else:
        # Show user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Get answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chain({"question": prompt})
                answer   = response["answer"]
                st.write(answer)
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": answer}
                )