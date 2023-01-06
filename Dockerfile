FROM python:3.12.0a3-slim-buster

RUN apt update -y && apt install -y build-essential libpq-dev && apt install zlib1g-dev libjpeg-dev libpng-dev -y
RUN pip install --upgrade pip
RUN pip install psycopg2-binary --no-binary psycopg2-binary


COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pillow

COPY ./api /app
WORKDIR /app
EXPOSE 8000

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
