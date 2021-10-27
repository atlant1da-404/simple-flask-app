FROM python:3.8

WORKDIR /application

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /application 

CMD ["python", "app.py"]