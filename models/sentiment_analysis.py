from transformers import pipeline


def perform_sentiment_analysis(text):
    print("Performing sentiment analysis for", text)
    sentiment_analysis = pipeline("sentiment-analysis", model="/app/cache/distilbert-base-uncased-finetuned-sst-2-english")
    return sentiment_analysis(text)
