FROM python:3.8.13

ENV PYTHONUNBUFFERED=1

USER root

RUN apt-get update && apt-get install -y apt-utils python3-dev

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
