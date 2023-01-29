from utils.pipelines_helper import from_pipeline
from utils.config import cache


@cache.memoize()
def perform_sentiment_analysis(text):
    print("Performing sentiment analysis for", text)
    sentiment_analysis = from_pipeline("sentiment-analysis")
    return sentiment_analysis(text)
