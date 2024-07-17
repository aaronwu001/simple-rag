from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader

def load_pdf_folder(folder_path):
    document_loader = PyPDFDirectoryLoader(folder_path)
    return document_loader.load()

# tsmc_folder_path = './tsmc-annual-report'
# document = load_pdf_folder(tsmc_folder_path)
# print(document[0])


# small_pdf_folder_path = './small-pdf'
# documents = load_pdf_folder(small_pdf_folder_path)
# print(documents[0])
# print('================================')
# print(documents[1])
# print('================================')
# print(len(documents))