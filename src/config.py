from pathlib import Path
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Vector store configuration
    db_location: Annotated[Path, Field(description="Location of the Chroma DB")] = Path(
        "./chroma_db"
    )
    embedding_model: Annotated[
        str, Field(description="Name of the embedding model to use")
    ] = "mxbai-embed-large"
    collection_name: Annotated[
        str, Field(description="Name of the vector store collection")
    ] = "restaurant_reviews"
    retriever_k: Annotated[
        int, Field(description="Number of results to retrieve", ge=1)
    ] = 5

    # Data configuration
    restaurants_file: Annotated[
        Path, Field(description="Path to the restaurants CSV file")
    ] = Path("restaurants.csv")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


# Create a global settings instance
SETTINGS = Settings()
