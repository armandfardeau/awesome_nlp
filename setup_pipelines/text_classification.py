from transformers import pipeline

pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
