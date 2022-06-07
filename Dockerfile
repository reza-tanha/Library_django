FROM python:latest
WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./config /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]