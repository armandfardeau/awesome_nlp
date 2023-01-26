from transformers import pipeline
from pillow import Image
import requests

def perform_image_classification(url):
    image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
    image = Image.open(requests.get(url, stream=True).raw)
    return image_classifier(image)