from flask import Flask, jsonify, request
from models.summarize import perform_summarize
from models.sentiment_analysis import perform_sentiment_analysis
from models.language_detection import perform_language_detection
from utils.translate import translate_request, perform_translate

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify(content="pong")


@app.route('/summarize', methods=['POST'])
def summarize():
    request_content = translate_request(request.get_json())
    response = perform_summarize(request_content['content'])
    translated_response = perform_translate(response[0]["summary_text"], source_lang="EN", target_lang=request_content['lang'])
    return jsonify(content=translated_response)


@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    request_content = translate_request(request.get_json())
    response = perform_sentiment_analysis(request_content['content'])
    return jsonify(content=response)


@app.route('/language-detection', methods=['POST'])
def language_detection():
    request_content = request.get_json()
    return jsonify(content=perform_language_detection(request_content['content']))
