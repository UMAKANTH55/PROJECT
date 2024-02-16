# Description: Dockerfile for the Flask application
FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app/

EXPOSE 3306

CMD ["python", "app.py"]

