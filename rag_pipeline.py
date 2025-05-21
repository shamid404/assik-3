from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
import os

def build_qa_chain(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(split_docs, embedding)

    llm = ChatOpenAI(
        openai_api_key=os.getenv("TOGETHER_API_KEY"),
        openai_api_base="https://api.together.xyz/v1",  # Together API base
        model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",  # или другой доступный через Together
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa_chain

