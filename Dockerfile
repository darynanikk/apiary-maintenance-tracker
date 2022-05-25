FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /apiary_service
WORKDIR /apiary_service
COPY . /apiary_service/
RUN python -m venv /venv/Scripts/activate
RUN pip install -r requirements.txt

