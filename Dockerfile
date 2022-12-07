FROM python:3.10

WORKDIR /.

COPY . .

RUN apt-get -y update
RUN apt-get install -y python3.10

RUN apt-get install -y ffmpeg

RUN pip3 install --user -r requirements.txt

RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install python-ffmpeg

#CMD ["python3", "app.py"]

CMD ["/bin/bash", "python3", "app.py"]