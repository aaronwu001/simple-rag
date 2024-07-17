from load import load_pdf_folder
from split import split_documents
from get_embedding_function import get_embedding_function
from chunks_indexing import index_chunks
from database import create_empty_db, get_db, update_db
import os
from rag_prompt_template import rag_prompt_template
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama


# load
pdf_folder_path = './source_pdf' 
documents = load_pdf_folder(pdf_folder_path)


# split
chunks = split_documents(documents)


# embedding
embedding_function = get_embedding_function()


# indexing the chunks 
# give each chunk an id of '{source}:{page}:{chunk}'
index_chunks(chunks)


persist_directory = './chroma_db'
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, persist_directory)

if os.path.isdir(folder_path):
    # if the folder exists, get the db.
    db = get_db(embedding_function, persist_directory)
else:
    # if the folder does not exist, create the db    
    db = create_empty_db(embedding_function, persist_directory)


# update the data base, inserting the chunks
# If no update, nothing happens.
update_db(db, chunks)


def query_rag(query_text):
    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(rag_prompt_template())
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)
    print("================")
    print(response_text)
    print("================")

    sources = [doc.metadata.get("id", None) for doc, _score in results]

    print("sources used")
    for source in sources:
        print(source)
        print('\n\n--\n\n')


question = "" # Replace with your question

query_rag(question)