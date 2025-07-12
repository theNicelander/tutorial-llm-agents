# Restaurant Review Vector Search

Based on tutorial: [@YouTube](https://www.youtube.com/watch?v=E4l91XKQSgw)

Vector search implementation for restaurant reviews using LangChain, Chroma DB, and Ollama embeddings.

## Setup

1. Install UV
2. Create `.env` file (optional, these are the defaults):

```env
DB_LOCATION=./chroma_db
EMBEDDING_MODEL=mxbai-embed-large
COLLECTION_NAME=restaurant_reviews
RETRIEVER_K=5
RESTAURANTS_FILE=restaurants.csv
```

## Run

```bash
uv run main.py
```
