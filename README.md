# Kazakhstan Constitution AI Assistant

An AI assistant for working with the Constitution of the Republic of Kazakhstan, built using RAG (Retrieval-Augmented Generation) architecture.

## Features

- Chat interface on Streamlit
- 📚 Download and indexing of PDF documents
- 🔍 Document context search
- 🤖 Using Mixtral-8x7B via the Together API
- Vector storage on ChromaDB

## Installation

1. Clone the repository:
``bash
git clone https://github.com/your-username/kazakhstan-constitution-ai.git
cd kazakhstan-constitution-ai
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key:

## Description
AI is an assistant who can answer questions on the Constitution of the Republic of Kazakhstan. PDF documents are loaded, indexed, and a RAG approach for generating responses is supported.

## Technologies used
- Streamlit
- Together API (LLM)
- ChromaDB
- LangChain

## Usage example
1. Download the PDF with the Constitution
2. Click on "Index Documents"
3. Enter the question in the input field
4. Get a response based on the context

## Screenshots
![img.png](img.png)_
![img_1.png](img_1.png)
![img_2.png](img_2.png)

## License
MIT