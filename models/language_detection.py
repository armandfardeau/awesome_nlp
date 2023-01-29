from utils.pipelines_helper import from_pipeline
from utils.config import cache


@cache.memoize()
def perform_language_detection(text):
    print("Performing language detection for", text)
    language_detection = from_pipeline("text-classification")
    return language_detection(text)
