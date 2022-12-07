FROM python:3.10

WORKDIR /app

COPY . . 

RUN apt-get -y update


RUN apt-get install -y ffmpeg

RUN python3 -m pip install --user -r requirements.txt

RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install ffmpeg-python

ENTRYPOINT [ "python3" ]

CMD ["app.py"]

#CMD ["python3", "app.py"]
#CMD ["/root/.local/lib/python3.10", "app.py"]