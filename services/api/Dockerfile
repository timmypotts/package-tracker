FROM python:3.8-slim-buster

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD exec gunicorn --bind :3080 --workers=2 --threads=4 --timeout 0 api:app