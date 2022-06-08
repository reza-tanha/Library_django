FROM python:latest

WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy data
COPY ./requirements.txt .
COPY ./config .
COPY ./entrypoint.sh .

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]