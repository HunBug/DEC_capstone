FROM python:3.9-slim-bookworm

WORKDIR /opt/dec_capstone

COPY wiki_reader .
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD [ "python", "kafka_producer.py"]
