from utils.pipelines_helper import from_pipeline
from PIL import Image
import requests
from utils.config import cache


@cache.memoize()
def perform_classify_image(url):
    print("Performing image classification for", url)
    image_classifier = from_pipeline("image-classification")
    image = Image.open(requests.get(url, stream=True).raw)
    return image_classifier(image)
