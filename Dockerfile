FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install software-properties-common

RUN add-apt-repository ppa:alex-p/tesseract-ocr

RUN apt-get update && \
    apt-get -y upgrade && \
    apt install -y tesseract-ocr tesseract-ocr-ukr

RUN apt-get update -y
RUN apt-get install -y python-pip
RUN pip install pytesseract

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]
