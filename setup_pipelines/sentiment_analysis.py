from transformers import pipeline

pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")