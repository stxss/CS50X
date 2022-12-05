FROM python:3.10

WORKDIR /clipcut

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /clipcut

CMD ["python3", "./clipcut/app.py"]

