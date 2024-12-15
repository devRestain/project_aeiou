FROM python:3.11.11-slim-bullseye

RUN pip install cmake poetry

WORKDIR /app/AEIOU
COPY ./AEIOU .

RUN poetry config virtualenvs.in-project true
RUN poetry config virtualenvs.path "./.venv"

RUN poetry init