from langchain_community.document_loaders import PyPDFLoader
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import InMemoryVectorStore


def get_embeddings_from_documents(document_paths: list[str], embedding: Embeddings) -> Embeddings:
    """Synchronous, slower (Not preferred)
    Usage example:
        embedding = get_embeddings_from_documents(
                    ["~/Documents/1.pdf", "~/Documents/2.pdf"],
                    OllamaEmbeddings(model="nomic-embed-text:latest")
        )
    """
    vector_store = InMemoryVectorStore(embedding=embedding)
    path: str
    for path in document_paths:
        vector_store.add_documents(list(PyPDFLoader(
                path,
                mode="page",
        ).lazy_load()))
    return vector_store.embeddings


async def aget_embeddings_from_documents(document_paths: list[str], embedding: Embeddings) -> Embeddings:
    """Asynchronous, much faster (preferred)
    Usage example:
        embedding = asyncio.run(aget_embeddings_from_documents(
                    ["~/Documents/1.pdf", "~/Documents/2.pdf"],
                    OllamaEmbeddings(model="nomic-embed-text:latest")
        ))
    """
    vector_store = InMemoryVectorStore(embedding=embedding)
    path: str
    processes = []
    for path in document_paths:
        processes.append(vector_store.aadd_documents(list(PyPDFLoader(
                path,
                mode="page",
        ).lazy_load())))
    for process in processes:
        await process
    return vector_store.embeddings
