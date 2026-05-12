from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import pdfplumber

from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

# ── 1. Load PDF ──────────────────────────────────────────────
def load_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# ── 2. Split into chunks ──────────────────────────────────────
def get_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_text(text)

# ── 3. Create Vector Store ────────────────────────────────────
def get_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_texts(chunks, embedding=embeddings)

# ── 4. API Key Helper ─────────────────────────────────────────
def get_groq_api_key():          # ✅ yeh naya function add karo
    try:
        return st.secrets["GROQ_API_KEY"]   # Streamlit Cloud
    except:
        return os.getenv("GROQ_API_KEY")    # Local .env

# ── 5. Build Conversational Chain with GROQ ───────────────────
def get_chain(vectorstore):
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=get_groq_api_key()          # ✅ yeh change karo
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        verbose=False
    )
    return chain