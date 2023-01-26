from transformers import pipeline


def perform_sentiment_analysis(text):
    sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return sentiment_analysis(text)
