from transformers import pipeline
from utils.config import cache


@cache.memoize()
def perform_question_answerer(content):
    print("Performing question answerer for", content)
    question = content['question']
    knowledge = content['knowledge']
    question_answerer = pipeline("question-answering", model="/app/cache/distilbert-base-uncased-distilled-squad")
    return question_answerer(question=question, context=knowledge)
