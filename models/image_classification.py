from transformers import pipeline
from pillow import Image
import requests

def perform_classify_image(url):
    image_classifier = pipeline("image-classification", model="./cache/vit-base-patch16-224")
    image = Image.open(requests.get(url, stream=True).raw)
    return image_classifier(image)