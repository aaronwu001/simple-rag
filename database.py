from langchain_community.vectorstores.chroma import Chroma


# def initialize_db(docs, embedding_function, persist_directory):
#     db = Chroma.from_documents(docs, embedding_function, persist_directory)
#     print("Chroma vector database created.")
#     return db


def create_empty_db(embedding_function, persist_directory):
    db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
    return db


def update_db(db, chunks):
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Original Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = [chunk for chunk in chunks if chunk.metadata["id"] not in existing_ids]
    if not new_chunks:
        print("No documents added.")
    else:
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
        print(f"Number of documents added: {len(new_chunk_ids)}")


def get_db(embedding_function, persist_directory):
    db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
    return db


def clear_db(persist_directory) -> bool:
    db = Chroma(persist_directory=persist_directory)
    if db:
        db.clear_documents()
        return True
    return False

