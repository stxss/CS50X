FROM python:3.10


WORKDIR /.

COPY . .

RUN apt-get -y update
RUN apt-get install -y ffmpeg
RUN pip3 install --no-cache-dir --user -r requirements.txt

RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install python-ffmpeg

ENTRYPOINT [ " /usr/bin/python3" ]

CMD ["python3","app.py"]