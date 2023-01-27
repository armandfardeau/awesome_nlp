from transformers import pipeline

pipeline("image-classification", model="google/vit-base-patch16-224")
