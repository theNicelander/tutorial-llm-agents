import os
from typing import Final

import pandas as pd
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_ollama import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from loguru import logger

from src.config import SETTINGS


def setup_restaurant_retriever() -> BaseRetriever:
    """Set up and return a vector store retriever for restaurant data."""
    embeddings = OllamaEmbeddings(model=SETTINGS.embedding_model)
    df = pd.read_csv(SETTINGS.restaurants_file)
    add_documents = not SETTINGS.db_location.exists()

    vector_store = Chroma(
        collection_name=SETTINGS.collection_name,
        persist_directory=str(SETTINGS.db_location),
        embedding_function=embeddings,
    )

    if add_documents:
        logger.info("Adding documents to vector store")
        documents = []
        ids = []
        for i, row in df.iterrows():
            title = row["Title"]
            review = row["Review"]
            rating = row["Rating"]
            date = row["Date"]

            document = Document(
                page_content=f"{title} ({rating} stars) + {review}",
                metadata={"rating": rating, "date": date},
                id=str(i),
            )
            ids.append(str(i))
            documents.append(document)

        vector_store.add_documents(documents)
        logger.success("Vector store setup complete")

    return vector_store.as_retriever(search_kwargs={"k": SETTINGS.retriever_k})
