from utils.pipelines_helper import from_pipeline
from utils.config import cache


@cache.memoize()
def perform_classify_text(text, labels, multi_label=False):
    print("Performing text classification for", text)
    text_classifier = from_pipeline("zero-shot-classification")
    return text_classifier(text, labels, multi_label=multi_label)
