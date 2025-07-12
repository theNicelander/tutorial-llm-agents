from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from loguru import logger

from src.vector import setup_restaurant_retriever

model = OllamaLLM(model="llama3.2")
retriever = setup_restaurant_retriever()

template = """
You are an expert in answering questions about a pizza restaurant reviews.
You do not give any further help, other than related to the reviews given
If there are no reviews given, say 'No reviews available.' and do not provide further information.
This is important, do not give any further information without the reviews given.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("-" * 50)
    question = input("Enter a question (q to quit): ").lower()
    clean_question = question.strip().replace("asdf", "")

    if clean_question == "q":
        logger.info("Quitting...")
        break

    reviews = retriever.invoke(clean_question)

    if "asdf" in question:
        for review in reviews:
            logger.debug(review.page_content)

    result = chain.invoke({"reviews": reviews, "question": clean_question})
    logger.info(result)
