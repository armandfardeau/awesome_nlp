from transformers import pipeline

pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")