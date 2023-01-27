from transformers import pipeline


def perform_language_detection(text):
    language_detection = pipeline("text-classification", model="./cache/papluca/xlm-roberta-base-language-detection")
    return language_detection(text)
