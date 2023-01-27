from transformers import pipeline
from utils.config import cache


@cache.memoize()
def perform_language_detection(text):
    print("Performing language detection for", text)
    language_detection = pipeline("text-classification", model="/app/cache/xlm-roberta-base-language-detection")
    return language_detection(text)
