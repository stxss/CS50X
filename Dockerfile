FROM python:3.10

ENV PYTHONPATH "${PYTHONPATH}:"

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

#COPY . /clipcut

CMD ["python3", "app.py"]

