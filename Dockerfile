FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN mkdir /kafka_producer

WORKDIR /kafka_producer

ADD ./src/ /kafka_producer/

RUN pip install -r requirements.txt

EXPOSE 8000