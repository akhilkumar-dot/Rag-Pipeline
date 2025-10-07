# 📄 PDF Question Answering Chatbot (RAG App with Telegram Bot + n8n Orchestration)

An intelligent **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDFs, extract content, and ask contextual questions — powered by **LangChain**, **Cohere**, **HuggingFace embeddings**, and **FAISS**.  
In addition to a Streamlit web app, it integrates a **Telegram bot automated via n8n** for seamless real-time conversational document Q&A across platforms.

---

## 🚀 Features

- 📤 **Upload PDFs** directly via Streamlit or Telegram bot  
- 🧠 **Chunk and embed** text using HuggingFace Sentence Transformers  
- 🪄 **Semantic search** powered by FAISS vector store  
- 🤖 **Answer generation** using Cohere’s `command-r-plus` LLM through LangChain’s RAG pipeline  
- 💬 **Real-time streaming responses** in chat-style interface  
- ⚙️ **n8n Orchestration:**  
  - Automates Telegram message reception, PDF upload handling, and API request flow  
  - Cleans responses with AI Transform nodes to fix Telegram formatting issues  
- 📱 **Telegram Bot Integration:**  
  - Users can send messages or upload PDFs directly in Telegram  
  - Bot forwards input to FastAPI `/chat` endpoint via n8n workflow  
  - Receives and sends AI-generated answers instantly back to chat  
- 🌐 **Deployment-ready** on Streamlit Cloud or Render

---

## 🧩 System Architecture

