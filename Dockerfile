FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN set -xe && apt-get -yqq update && apt-get -yqq install python3-pip && pip3 install --upgrade pip && pip install -r requirements.txt

COPY ./ ./

WORKDIR /app/src

CMD ["python", "./demo_usage.py"]
