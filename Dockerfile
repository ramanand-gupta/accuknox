FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /accuknox

COPY requirements.txt /accuknox/

RUN pip install -r requirements.txt

COPY . /accuknox/
