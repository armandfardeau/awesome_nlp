from transformers import pipeline


def perform_summarize(text):
    print("Performing summarization for", text)
    summarizer = pipeline("summarization", model="/app/cache/bart-large-cnn")
    return summarizer(text, max_length=130, min_length=30, do_sample=False)
