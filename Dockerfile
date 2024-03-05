FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt

COPY ./entrypoint.sh .

COPY . /usr/src/app/

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
