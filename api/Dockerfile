FROM python:3.9-buster

RUN mkdir api
WORKDIR /api

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

#RUN echo "installing fastapi and dependcies"
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY main.py .