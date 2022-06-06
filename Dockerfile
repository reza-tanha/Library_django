FROM python:latest
RUN pip install --upgrade pip
RUN apt install -y gcc
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./config /app
WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]