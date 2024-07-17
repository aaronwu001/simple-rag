def rag_prompt_template():
    
    template = """
    Anawer the question based only on the following context:
    {context}

    ---
    Answer the question based on the above contet: {question}
    """

    return template