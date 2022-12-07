FROM python:3.10

WORKDIR /.

COPY . /. 
EXPOSE 8080


ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH "${PYTHONPATH}:/."

RUN apt-get -y update


RUN apt-get install -y ffmpeg
#RUN pip install --user -r requirements.txt
RUN python3 -m pip install --user -r requirements.txt



RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install ffmpeg-python

#ENTRYPOINT ["/usr/bin/python3", "app.py"]

#CMD ["/usr/bin/python3", "app.py"]

#ENTRYPOINT [ "/usr/bin/python3" ]
#CMD ["/app.py"]

CMD ["python3", "app.py"]


#CMD ["/root/.local/lib/python3.10", "app.py"]