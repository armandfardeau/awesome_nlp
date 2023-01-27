from transformers import pipeline


def perform_text_generation(text, max_length=50, do_sample="False"):
    sample = True if do_sample == "True" else False
    text_generator = pipeline("text-generation", model="./cache/gpt-j-6B")
    return text_generator(text, max_length=max_length, do_sample=sample)
