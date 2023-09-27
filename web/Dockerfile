FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY  . /code/
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations