from flask import Flask, jsonify, request
from summarize import perform_summarize
from sentiment_analysis import perform_sentiment_analysis

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
