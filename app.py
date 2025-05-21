import streamlit as st
from dotenv import load_dotenv
from document_loader import load_documents
from rag_pipeline import build_qa_chain

load_dotenv()

st.set_page_config(page_title="Kazakhstan Constitution AI Assistant")
st.title("🇰🇿 Kazakhstan Constitution AI Assistant")

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

uploaded_files = st.file_uploader("Upload documents (PDF)", accept_multiple_files=True, type=["pdf"])

if st.button("Index Documents"):
    if uploaded_files:
        try:
            with st.spinner("Indexing..."):
                docs = load_documents(uploaded_files)
                if docs:
                    st.session_state.qa_chain = build_qa_chain(docs)
                    st.success("Documents indexed successfully!")
                else:
                    st.error("No documents were loaded. Please check your PDF files.")
        except Exception as e:
            st.error(f"Error during indexing: {str(e)}")
    else:
        st.warning("Please upload at least one PDF file.")

query = st.text_input("Ask a question about the Constitution or uploaded documents:")

if query and st.session_state.qa_chain:
    with st.spinner("Thinking..."):
        result = st.session_state.qa_chain.run(query)
        st.write("Answer:")
        st.success(result)
