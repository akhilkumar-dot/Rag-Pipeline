# 📄 PDF Question Answering Chatbot (RAG App)

An interactive Streamlit web app that lets you upload a PDF, extracts its content, and answers your questions using **LangChain**, **Cohere's command-r-plus**, **FAISS**, and **HuggingFace embeddings**. It features **real-time streamed answers**, making it feel like a true AI chat experience.

---

## 🚀 Features

- 📤 Upload any PDF file
- 🧠 Chunk the PDF and embed using HuggingFace transformers
- 🔍 Store and retrieve relevant chunks using FAISS vector store
- 🤖 Answer user questions using Cohere’s `command-r-plus` LLM
- 💬 Real-time chat-style streamed responses
- 🌐 Easy to deploy on Streamlit Cloud

---

## 🛠️ Tech Stack

| Layer        | Tool |
|--------------|------|
| Frontend UI  | Streamlit |
| LLM          | Cohere (command-r-plus) |
| Embeddings   | HuggingFace Sentence Transformers |
| RAG Engine   | LangChain (RetrievalQA) |
| Vector Store | FAISS |
| PDF Parsing  | PyPDF |

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/pdf-qa-chatbot.git
cd pdf-qa-chatbot
