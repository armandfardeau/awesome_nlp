from transformers import pipeline


def perform_question_answerer(content):
    question = content['question']
    knowledge = content['knowledge']
    question_answerer = pipeline("question-answering", model="./cache/distilbert-base-uncased-distilled-squad")
    return question_answerer(question=question, context=knowledge)
