FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN set -xe && apt-get -yqq update && apt-get -yqq install python3-pip
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip3 install --upgrade pip && pip install -r requirements.txt

COPY ./ ./

WORKDIR /app/src

CMD ["python", "./demo_usage.py"]
