FROM alpine:3.17 as builder

RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl tzdata alpine-conf
RUN adduser -D dbs

RUN setup-timezone -z Europe/Bratislava

USER dbs

WORKDIR /home/dbs

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD /home/dbs/.local/bin/uvicorn dbs_assignment.__main__:app --reload --host 0.0.0.0
