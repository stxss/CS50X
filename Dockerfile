FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----
#RUN python3 -m pip install ffmpeg-python
#RUN python3 -m pip install python-ffmpeg
RUN pip install python-ffmpeg
#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]