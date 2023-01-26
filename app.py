from flask import Flask, jsonify, request
from models.summarize import perform_summarize
from models.sentiment_analysis import perform_sentiment_analysis
from models.language_detection import perform_language_detection

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify(content="pong")


@app.route('/summarize', methods=['POST'])
def summarize():
    request_content = request.get_json()
    return jsonify(content=perform_summarize(request_content['content']))


@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    request_content = request.get_json()
    return jsonify(content=perform_sentiment_analysis(request_content['content']))


@app.route('/language-detection', methods=['POST'])
def language_detection():
    request_content = request.get_json()
    return jsonify(content=perform_language_detection(request_content['content']))

@app.route('/translate', methods=['POST'])
def translate():
    request_content = request.get_json()
    return jsonify(content=perform_translate(request_content['content']))