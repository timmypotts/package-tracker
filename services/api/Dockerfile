FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD exec gunicorn --bind :3080 --workers=2 --threads=4 --timeout 0 run:app