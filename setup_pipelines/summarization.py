from transformers import pipeline

pipeline("summarization", model="facebook/bart-large-cnn")
