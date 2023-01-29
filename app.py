import os
from flask import Flask, request
from utils.config import cache, config
from models.summarize import perform_summarize
from models.sentiment_analysis import perform_sentiment_analysis
from models.language_detection import perform_language_detection
from models.question_answerer import perform_question_answerer
from models.text_generation import perform_text_generation
from models.image_classification import perform_classify_image
from utils.translate import translate_request, perform_translate
from utils.pipelines_helper import preload_pipelines, pipeline_file

app = Flask(__name__)
cache.init_app(app, config=config)
if os.environ.get('PRELOAD_PIPELINES') == 'true':
    preload_pipelines()


@cache.cached()
@app.route('/ping')
def ping():
    return {"content": "pong"}


@cache.cached()
@app.route('/')
def root():
    return {"content": str(pipeline_file())}


@app.route('/summarize', methods=['POST'])
def summarize():
    request_content = translate_request(request.get_json())
    response = perform_summarize(request_content['content'])
    translated_response = perform_translate(response[0]["summary_text"], source_lang="en",
                                            target_lang=request_content['lang'])
    return {"content": translated_response}


@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    request_content = translate_request(request.get_json())
    return {"content": perform_sentiment_analysis(request_content['content'])}


@app.route('/language-detection', methods=['POST'])
def language_detection():
    request_content = request.get_json()
    return {"content": perform_language_detection(request_content['content'])}


@app.route('/question-answerer', methods=['POST'])
def answer():
    request_content = request.get_json()
    question = translate_request({'content': request_content['content']['question']})
    knowledge = translate_request({'content': request_content['content']['knowledge']})
    lang = question['lang']
    response = perform_question_answerer({"question": question['content'], "knowledge": knowledge['content']})
    translated_response = perform_translate(response["answer"], source_lang="en", target_lang=lang)
    return {"content": translated_response}


@app.route('/generate-text', methods=['POST'])
def generate():
    request_content = translate_request(request.get_json())
    response = perform_text_generation(request_content['content'], request_content['max_length'])
    translated_response = perform_translate(response[0]["generated_text"], source_lang="en",
                                            target_lang=request_content['lang'])
    return {"content": translated_response}


@app.route('/classify-image', methods=['POST'])
def classify_image():
    request_content = request.get_json()
    return {"content": perform_classify_image(request_content['content'])}
