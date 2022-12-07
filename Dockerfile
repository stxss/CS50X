FROM python:3.9

RUN mkdir /app
WORKDIR /app

#----
RUN sudo apt install ffmpeg
#----


COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----
RUN pip install ffmpeg-python
#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]