FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt

COPY . .

RUN pip3 install ffmpeg-python

ENTRYPOINT ["/usr/bin/python3", "./app.py" ]