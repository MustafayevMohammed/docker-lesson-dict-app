FROM python:3.9.6-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . .

COPY ./requirements.txt requirements.txt
RUN pip3 install --upgrade pip
# RUN systemctl start docker
RUN apk add python3-dev libffi-dev libressl-dev libuv-dev build-base
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r requirements.txt
RUN apk del .tmp

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
