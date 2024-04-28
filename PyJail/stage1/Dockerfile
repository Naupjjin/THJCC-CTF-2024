FROM alpine/socat

RUN apk add --no-cache python3 py3-pip \
    && adduser -D restricted_user

RUN python3 -m venv /opt/pyjail1

RUN mkdir -p /app \
    && chown restricted_user:restricted_user /app \
    && chmod 500 /app

WORKDIR /app

COPY ./src /app/

USER restricted_user

EXPOSE 40001
ENTRYPOINT ["socat", "tcp-listen:40001,fork", "EXEC:'/opt/pyjail1/bin/python server.py'"]