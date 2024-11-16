# Simple-RAG (Retrieval-Augmented Generation)

**Simple-RAG** is a lightweight implementation of a Retrieval-Augmented Generation (RAG) system designed to run entirely locally. By combining document retrieval and language model generation, it allows for accurate and context-aware responses to user queries using a locally hosted LLM. The project uses LangChain, ChromaDB, and the Llama3 model for efficient retrieval and generation.

## 🚀 Project Overview

**Simple-RAG** enables:
1. **Document Retrieval**: Efficiently searches a vector database for relevant context from indexed documents.
2. **Augmented Generation**: Uses retrieved context to generate precise answers with a local language model.
3. **Local-Only Setup**: No external API calls—everything runs on your local machine for privacy and security.
4. The project uses LLama3 as the local LLM powering the project. Feel free to change it to other LLMs.

## 🛠 Features

### **Core Functionalities**
1. **PDF Document Loading**: Loads and processes PDF files from the `source_pdf` folder.
2. **Text Splitting**: Splits documents into smaller chunks with overlap to ensure context is preserved.
3. **Chunk Indexing**: Assigns unique IDs to chunks based on their source, page, and chunk number.
4. **Vector Database Management**: Manages document embeddings using ChromaDB for fast similarity search.
5. **Local Language Model Integration**: Uses Llama3 as the local LLM for query response generation.
6. **Modular Design**: Easily customizable to work with other LLMs or document formats.

## 🛠 Tech Stack

- **Language Models**:
  - [Llama3 (via Ollama)](https://ollama.com/) for local LLM inference.
- **Document Processing**:
  - `PyPDFDirectoryLoader` for PDF loading.
  - `RecursiveCharacterTextSplitter` for chunking.
- **Vector Database**:
  - [ChromaDB](https://docs.trychroma.com/) for document embeddings and similarity search.
- **Embedding Generation**:
  - Ollama's Llama3 embedding model for high-quality embeddings.
- **Frameworks and Tools**:
  - LangChain for chaining document retrieval and generation tasks.
  - Python 3.12
  - Poetry for dependency management.

## 🌟 What the Project Does

1. **Document Loading**:
   - The `load_pdf_folder()` function loads PDF files from the `source_pdf` folder.
2. **Text Splitting**:
   - Splits documents into smaller chunks using `split_documents()` (adjustable chunk size and overlap).
3. **Chunk Indexing**:
   - Each chunk is assigned a unique ID (`source:page:chunk`).
4. **Embedding**:
   - Generates embeddings for chunks using Llama3.
5. **Vector Database**:
   - Creates or updates a Chroma vector database (`chroma_db` folder).
6. **Querying**:
   - Queries the vector database and retrieves relevant chunks.
   - Passes the context and query to the local Llama3 model for response generation.
   - Outputs the response and the sources used.

## 📚 Lessons Learned

### Challenges:
- Ensuring embeddings and document IDs align correctly during updates.
- Maintaining a fully modular pipeline to simplify debugging and scaling.

### Lessons:
- Effective chunking and overlap significantly improve retrieval accuracy.
- Local-only setups ensure privacy but require resource management.

## 🔮 Future Improvements

1. **Interactive Web Interface**:
   - Build a web-based UI for querying and exploring results.
2. **Multi-Language Support**:
   - Add support for non-English documents and queries.
3. **Cloud Deployment**:
   - Deploy the system on AWS or GCP for larger-scale applications.
4. **Custom Prompt Engineering**:
   - Add domain-specific templates for generating more accurate answers.
5. **Real-Time Updates**:
   - Enable dynamic updates to the database as new files are added.

## 🛠 Acknowledgments

This project is inspired by Pixegami's [YouTube tutorial](https://www.youtube.com/watch?v=2TJxpyO3ei4&t=396s) and serves as a personal implementation of a Local RAG pipeline with LangChain.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🌐 Additional Resources

- **LangChain Documentation**: [LangChain Docs](https://docs.langchain.com/)
- **ChromaDB Documentation**: [ChromaDB Docs](https://docs.trychroma.com/)
- **Ollama Llama3**: [Ollama](https://ollama.com/)
- **Pixegami Tutorial**: [YouTube Link](https://www.youtube.com/watch?v=2TJxpyO3ei4&t=396s)
- **PDF Parsing**: [PyPDF Docs](https://pypdf2.readthedocs.io/en/latest/)


## 📋 Set-Up Guide

### **Prerequisites**
1. **Install Poetry**:
   - Poetry is required for dependency management. Install it using:
     ```bash
     pip install poetry
     ```

2. **Install Ollama**:
   - Download and install Ollama from [here](https://ollama.com/).

3. **System Requirements**:
   - Python 3.12 or later.
   - A machine with sufficient resources to run the Llama3 model locally.

### **Installation Steps**

Set-up Guide:
1. Install Poetry. run 'poetry shell', 'poetry lock', then 'poetry udpate' in the root directory to set up the environment and dependencies.
2. Install Ollama. run 'Ollama pull llama3' to install the Llama3 model (modify the code for different models)
3. Run 'Ollama serve' to run the model as a server at localhost:11434.
4. Find pdf files for the RAG project and put them in the 'source_pdf' folder in the root directory.
4. Find the empty question string at the bottom of file 'query_rag'. Replace it with your question.
5. Run 'python query_rag' in the terminal to see the response.

What the project does:
1. loads your pdf file from the 'source_pdf' folder (load.py)
2. splits your pdf file (you can adjust the parameters in split.py)
3. index the split documents (chunks) using the their source, page, and chunk number (chunks_indexing.py)
4. do embedding on the split documents using the local Llama3 model. (get_embedding_function.py)
5. if not already, create a Chroma vector database with folder name 'chroma_db' in your root directory.
6. update the database with new files in the 'source_pdf' folder
7. query your local LLM (Llama3) and print the response text as well as what sources are used. 

