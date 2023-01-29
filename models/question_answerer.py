from utils.pipelines_helper import from_pipeline
from utils.config import cache


@cache.memoize()
def perform_question_answerer(content):
    print("Performing question answerer for", content)
    question = content['question']
    knowledge = content['knowledge']
    question_answerer = from_pipeline("question-answering")
    return question_answerer(question=question, context=knowledge)
