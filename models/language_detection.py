from transformers import pipeline


def perform_language_detection(text):
    language_detection = pipeline("text-classification", model="/app/cache/xlm-roberta-base-language-detection")
    return language_detection(text)
