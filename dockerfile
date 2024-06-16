FROM python:3.11.3-slim-buster

WORKDIR /app

RUN pip install scrapy psycopg2 pymongo
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY spiders/ ./spiders/
COPY pipelines.py ./pipelines.py

CMD ["scrapy", "crawl", "job_spider"]