from utils.pipelines_helper import from_pipeline
from utils.config import cache


@cache.memoize()
def perform_text_generation(text, max_length=50, do_sample="False"):
    print("Performing text generation for", text)
    sample = True if do_sample == "True" else False
    text_generator = from_pipeline("text-generation")
    return text_generator(text, max_length=max_length, do_sample=sample)
