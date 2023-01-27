from transformers import pipeline


def perform_summarize(text):
    summarizer = pipeline("summarization", model="./cache/bart-large-cnn")
    return summarizer(text, max_length=130, min_length=30, do_sample=False)
