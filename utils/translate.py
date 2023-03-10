import os
import requests
import json
from models.language_detection import perform_language_detection
from utils.config import cache


@cache.memoize()
def send_request(text, source_lang, target_lang="en"):
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key == '' or api_key is None:
        raise Exception("DEEPL_API_KEY is not set")

    url = "https://api-free.deepl.com/v2/translate"

    payload = json.dumps({"source_lang": source_lang,"target_lang": target_lang,"text": [text]})

    headers = {'Authorization': api_key,'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    print("Translation response", response.text, response.status_code)
    return response.text


@cache.memoize()
def perform_translate(text, source_lang, target_lang="en"):
    if source_lang == target_lang:
        return text

    response_text = send_request(text, source_lang, target_lang)
    return json.loads(response_text)['translations'][0]['text']


@cache.memoize()
def translate_request(request_content):
    if "lang" in request_content:
        lang = request_content['lang']
    else:
        lang = perform_language_detection(request_content['content'])[0]['label']
        request_content['lang'] = lang

    if lang != "en":
        request_content['content'] = perform_translate(request_content['content'], lang)

    return request_content
