from langchain.vectorstores import Chroma, VectorStore
from langchain.embeddings import HuggingFaceEmbeddings


def get_database() -> VectorStore:
    # TODO: reuse existing db if necessary
    # TODO: set up correctly, e.g. collection_name, etc.

    # TODO: source config elsewhere
    # TODO: try out Instructor embedding
    #  - https://instructor-embedding.github.io/
    #  - https://huggingface.co/hkunlp/instructor-large
    #  - https://huggingface.co/hkunlp/instructor-xl
    #  - https://python.langchain.com/en/latest/modules/models/text_embedding/examples/instruct_embeddings.html
    embeddings_model_name = "all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    return Chroma(embedding_function=embeddings)
