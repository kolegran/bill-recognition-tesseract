FROM ubuntu:16.04

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python-pip

RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install software-properties-common

RUN add-apt-repository ppa:alex-p/tesseract-ocr

RUN apt-get update && \
    apt-get -y upgrade && \
    apt install -y tesseract-ocr tesseract-ocr-ukr

ENTRYPOINT ["python"]

CMD ["app.py"]
