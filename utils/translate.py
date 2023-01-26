import os
import requests
import json


def send_request(text, source_lang, target_lang="EN"):
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key is None:
        raise Exception("DEEPL_API_KEY is not set")

    url = "https://api-free.deepl.com/v2/translate"

    payload = json.dumps({
        "source_lang": source_lang,
        "target_lang": target_lang,
        "text": [
            text
        ]
    })

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


def perform_translate(text, source_lang, target_lang="EN"):
    response = send_request(text, source_lang, target_lang)
    return response.json()['translations'][0]['text']
