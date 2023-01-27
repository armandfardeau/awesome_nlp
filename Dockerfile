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

COPY . .

EXPOSE 8080

CMD gunicorn --bind 0.0.0.0:$PORT --workers $WORKERS --access-logfile - --error-logfile - --log-level debug --timeout $TIMEOUT wsgi:app