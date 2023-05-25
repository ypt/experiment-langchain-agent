from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import VectorStore
from langchain.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PDFMinerLoader,
    TextLoader,
    # UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)

LOADER_EXTENSION_MAP = {
    "csv": (CSVLoader, {}),
    # "docx": (Docx2txtLoader, {}),
    "doc": (UnstructuredWordDocumentLoader, {}),
    "docx": (UnstructuredWordDocumentLoader, {}),
    "enex": (EverNoteLoader, {}),
    # "eml": (MyElmLoader, {}),
    "epub": (UnstructuredEPubLoader, {}),
    "html": (UnstructuredHTMLLoader, {}),
    "md": (UnstructuredMarkdownLoader, {}),
    "odt": (UnstructuredODTLoader, {}),
    "pdf": (PDFMinerLoader, {}),
    "ppt": (UnstructuredPowerPointLoader, {}),
    "pptx": (UnstructuredPowerPointLoader, {}),
    "txt": (TextLoader, {"encoding": "utf8"}),
}

text_splitter_chunk_size = 500
text_splitter_chunk_overlap = 50


def get_loader(file_path: str):
    ext = file_path.rsplit(".", 1)[-1]
    if ext in LOADER_EXTENSION_MAP:
        loader_class, loader_args = LOADER_EXTENSION_MAP[ext]
        return loader_class(file_path, **loader_args)

    return None


def process_document(database: VectorStore, file_path: str) -> List[Document]:
    loader = get_loader(file_path)
    if loader is None:
        raise ValueError(f"Unsupported file type")

    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=text_splitter_chunk_size,
                                                   chunk_overlap=text_splitter_chunk_overlap)
    texts = text_splitter.split_documents(documents)

    database.add_documents(texts)
    return texts
