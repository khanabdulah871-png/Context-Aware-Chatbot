# 📄 Context-Aware PDF Chatbot

A conversational chatbot that answers questions from uploaded PDF documents using RAG (Retrieval-Augmented Generation), LangChain, GROQ, and Streamlit.

---

## 🚀 Live Demo
[Click Here](https://khanabdulah871-png-context-aware-chatbot-app-xxxxx.streamlit.app)

---

## 🧠 How It Works

PDF → Text Chunks → Embeddings → FAISS Vector Store
↓
User Question → Retriever → GROQ LLM → Answer
↑
Conversation Memory

---

## ⚙️ Features

- 📂 Upload any PDF document
- 🔍 Semantic search using FAISS
- 🧠 Context-aware conversation memory
- ⚡ Fast responses powered by GROQ
- 🎛️ Adjustable response creativity (temperature)
- 🌐 Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| LangChain | RAG pipeline |
| GROQ (LLaMA 3.3) | LLM responses |
| FAISS | Vector store |
| HuggingFace | Embeddings |
| pdfplumber | PDF reading |
| Streamlit | Frontend UI |

---

## 📁 Project Structure

Context-Aware-Chatbot/
├── app.py               # Streamlit frontend
├── rag_pipeline.py      # RAG logic
├── main.py              # PDF loader
├── .env                 # API keys (local only)
├── requirements.txt     # Dependencies
└── README.md            # This file

---

## 🔧 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/khanabdulah871-png/Context-Aware-Chatbot.git
cd Context-Aware-Chatbot
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Key
Create `.env` file:

GROQ_API_KEY=your_groq_api_key_here

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🔑 Get GROQ API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up and create API key
3. Paste in `.env` file

---

## 👤 Author

**Muhammad Abdullah Khan**  
[GitHub](https://github.com/khanabdulah871-png) • [LinkedIn](https://www.linkedin.com/in/muhammad-abdullah-khan-6a3696287/)

