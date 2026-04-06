from document_embedding import  aget_embeddings_from_documents
import asyncio
from langchain_ollama import OllamaEmbeddings


embedding = asyncio.run(aget_embeddings_from_documents(
            ["~/Documents/1.pdf", "~/Documents/2.pdf"],
            OllamaEmbeddings(model="nomic-embed-text:latest")
))
print(embedding)
