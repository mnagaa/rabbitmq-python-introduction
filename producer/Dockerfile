FROM python:3.7

RUN mkdir /producer
WORKDIR /producer

COPY ./producer/requirements.txt /producer/requirements.txt
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 6666
ENV PYTHONPATH "${PYTHONPATH}:/producer/"

ENV LANG 'ja_JP.UTF-8'