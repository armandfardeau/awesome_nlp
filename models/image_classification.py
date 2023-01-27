from transformers import pipeline
from PIL import Image
import requests
from utils.config import cache


@cache.memoize()
def perform_classify_image(url):
    print("Performing image classification for", url)
    image_classifier = pipeline("image-classification", model="/app/cache/vit-base-patch16-224")
    image = Image.open(requests.get(url, stream=True).raw)
    return image_classifier(image)
