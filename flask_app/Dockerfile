FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD flask_app/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD flask_app /code/
ENV FLASK_APP=appinit