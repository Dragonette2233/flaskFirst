FROM python:3.9.2-alpine

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP ./fufo_main

CMD ["waitress-serve", "--call", "fufo_main:create_app"]