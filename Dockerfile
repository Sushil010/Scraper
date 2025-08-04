FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y wget gnupg unzip curl && \
    apt-get install -y chromium chromium-driver

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_BIN=/usr/bin/chromedriver

WORKDIR /app

COPY . /app


RUN pip install selenium


CMD ["python", "main.py"]
