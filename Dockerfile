FROM python:3.11.2-alpine3.17

RUN pip install flask

RUN apk add aws-cli

COPY . /opt/

EXPOSE 8080

WORKDIR /opt

ENTRYPOINT ["python", "app.py"]
