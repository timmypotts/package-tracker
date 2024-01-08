# FROM python:3.8-slim-buster

# WORKDIR /app
# COPY . .

# RUN apt-get update && \
#     apt-get install -y gcc libpq-dev && \
#     curl -sSL https://install.python-poetry.org | python3 - \
#     poetry install --no-root \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# CMD ["poetry", "run", "python", "run.py"]


# The builder image, used to build the virtual environment
FROM python:3.11-buster as builder

RUN pip install poetry==1.4.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY . .
RUN touch README.md

RUN poetry install --without dev

ENTRYPOINT ["poetry", "run", "python", "-m", "run"]