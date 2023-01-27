FROM python:3.10

ENV PYTHONUNBUFFERED=1 \
PORT=8080 \
FLASK_DEBUG="false" \
TIMEOUT=120 \
WORKERS=1 \
TRANSFORMERS_CACHE="/tmp/transformers"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY setup_pipelines/image_classification.py ./setup_pipelines/
RUN python setup_pipelines/image_classification.py

COPY setup_pipelines/question_answering.py ./setup_pipelines/
RUN python setup_pipelines/question_answering.py

COPY setup_pipelines/sentiment_analysis.py ./setup_pipelines/
RUN python setup_pipelines/sentiment_analysis.py

COPY setup_pipelines/summarization.py ./setup_pipelines/
RUN python setup_pipelines/summarization.py

COPY setup_pipelines/text_classification.py ./setup_pipelines/
RUN python setup_pipelines/text_classification.py

COPY setup_pipelines/text_generation.py ./setup_pipelines/
RUN python setup_pipelines/text_generation.py

COPY . .

EXPOSE 8080

CMD gunicorn --bind 0.0.0.0:$PORT --workers $WORKERS --access-logfile - --error-logfile - --log-level debug --timeout $TIMEOUT wsgi:app