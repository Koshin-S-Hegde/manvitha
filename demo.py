from document_embedding import  aget_vectordb_from_documents
import asyncio
from langchain_ollama import OllamaEmbeddings


vectordb = asyncio.run(aget_vectordb_from_documents(
            ["~/Documents/1.pdf", "~/Documents/2.pdf"],
            OllamaEmbeddings(model="nomic-embed-text:latest"),
))
print(vectordb)
