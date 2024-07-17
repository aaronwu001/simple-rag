# Local RAG with Langchain

This is a sample project of running RAG completely locally using Langchain.
This is not a chatbot. 

The project uses LLama3 as the local LLM powering the project. 
It can be changed to any other LLM. 

How-to Guide:
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

## Acknowledgments

This project is my personal attempt based on the Youtube video by pixegami. The video can be found [here](https://www.youtube.com/watch?v=2TJxpyO3ei4&t=396s).