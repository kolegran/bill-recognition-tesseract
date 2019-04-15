FROM ubuntu:latest

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python-pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]