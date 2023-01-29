from utils.pipelines_helper import from_pipeline
from utils.config import cache


@cache.memoize()
def perform_summarize(text):
    print("Performing summarization for", text)
    summarizer = from_pipeline("summarization")
    return summarizer(text, max_length=130, min_length=30, do_sample=False)
