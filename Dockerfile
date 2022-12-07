FROM python:3.10

WORKDIR /app

COPY . . 

ENV PATH=/root/.local/bin:$PATH

RUN apt-get -y update

RUN apt-get install -y ffmpeg
RUN python3 -m pip install --user -r requirements.txt

RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install ffmpeg-python

CMD ["/usr/bin/python3", "app/app.py"]

EXPOSE 8080

