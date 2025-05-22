FROM python:3.10

WORKDIR /app

COPY worker.py .

RUN pip install pika

CMD ["python", "worker.py"]
