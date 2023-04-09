FROM python:3.9.2-alpine

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP ./fufo_main
ENV FLASK_ENV production

CMD ["flask", "run", "--host=0.0.0.0"]