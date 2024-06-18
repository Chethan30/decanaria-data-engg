# TODO: Run tests in a separate container

FROM python:3.10-slim-bullseye

WORKDIR /app

# RUN pip install scrapy psycopg2 pymongo
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY jobs_project/ ./jobs_project/

COPY data_src/ ./data_src/

CMD ["sh", "-c", "cd jobs_project/jobs_project/spiders && scrapy runspider json_spider.py"]