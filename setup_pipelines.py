from transformers import pipeline

pipeline("summarization", model="facebook/bart-large-cnn")
pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
