import streamlit as st
from langchain_community.chat_models import ChatCohere
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import tempfile
import os

# ----------------------------------
# ✅ PATCH to fix .token_count error
# ----------------------------------
def patched_get_generation_info(self, response):
    return {
        "id": getattr(response, "id", None),
        "response_id": getattr(response, "response_id", None),
    }

ChatCohere._get_generation_info = patched_get_generation_info

# ----------------------------------
# Streamlit App Config
# ----------------------------------
st.set_page_config(page_title="📄 PDF Chatbot", layout="wide")
st.title("📄 Ask Questions About Your PDF")

# Sidebar: API Key
cohere_api_key = st.sidebar.text_input("🔑 Enter your Cohere API Key", type="password")
if not cohere_api_key:
    st.sidebar.warning("Please enter your Cohere API key to proceed.")
    st.stop()

# Upload PDF
uploaded_file = st.file_uploader("📁 Upload a PDF file", type="pdf")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_pdf_path = tmp_file.name

    # -----------------------
    # Step 1: Load & Split PDF
    # -----------------------
    loader = PyPDFLoader(tmp_pdf_path)
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150
    )
    documents = text_splitter.split_documents(pages)

    # -----------------------
    # Step 2: Embedding
    # -----------------------
    st.info("🔍 Embedding the document...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embedding_model)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # -----------------------
    # Step 3: LLM Setup
    # -----------------------
    llm = ChatCohere(cohere_api_key=cohere_api_key, model="command-r-plus", temperature=0.3)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    # -----------------------
    # Step 4: Ask a Question
    # -----------------------
    question = st.text_input("❓ Ask a question about the PDF:")
    if question:
        with st.spinner("💡 Generating answer..."):
            result = qa_chain(question)
            st.subheader("🧠 Answer:")
            st.write(result["result"])

            with st.expander("📄 Source Chunks"):
                for doc in result["source_documents"]:
                    st.markdown(doc.page_content)

    # Clean up temp PDF
    os.remove(tmp_pdf_path)
