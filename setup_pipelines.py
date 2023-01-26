from transformers import pipeline

pipeline("summarization", model="facebook/bart-large-cnn")
pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
