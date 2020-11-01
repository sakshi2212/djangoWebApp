FROM python:3.8
 
ENV PYTHONUNBUFFERED 1

RUN mkdir /Assignment

COPY requirements.txt /Assignment/

WORKDIR /Assignment

RUN pip install -r requirements.txt

COPY . /Assignment/
