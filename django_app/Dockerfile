FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD django_app/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD django_app /code/
