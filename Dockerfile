FROM python:3.9.20-slim-buster

WORKDIR /stream

COPY . /stream

RUN pip install -r requirements.txt

CMD ["python3", "stream.py"]
