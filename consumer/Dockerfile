FROM python:3.7

RUN mkdir /consumer
WORKDIR /consumer

COPY ./consumer/requirements.txt /consumer/requirements.txt
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 6666
ENV PYTHONPATH "${PYTHONPATH}:/consumer/"

ENV LANG 'ja_JP.UTF-8'