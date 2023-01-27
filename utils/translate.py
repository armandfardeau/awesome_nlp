import os
import requests
import json
from models.language_detection import perform_language_detection


def send_request(text, source_lang, target_lang="EN"):
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key is None:
        raise Exception("DEEPL_API_KEY is not set")

    url = "https://api-free.deepl.com/v2/translate"

    payload = json.dumps({
        "source_lang": source_lang,
        "target_lang": target_lang,
        "text": [text]
    })

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def perform_translate(text, source_lang, target_lang="EN"):
    if source_lang == target_lang:
        return text

    response_text = send_request(text, source_lang, target_lang)
    print(response_text)
    return json.loads(response_text)['translations'][0]['text']


def translate_request(request_content):
    lang = perform_language_detection(request_content['content'])[0]['label']

    if lang != "EN" or lang != "en":
        request_content['content'] = perform_translate(request_content['content'], lang)
        request_content['lang'] = lang
    else:
        request_content['lang'] = "EN"

    return request_content
