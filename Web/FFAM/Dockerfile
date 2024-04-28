FROM python:3.8-slim


RUN python3 -m venv /opt/ffam

RUN mkdir -p /app
WORKDIR /app

COPY ./src /app/
RUN /opt/ffam/bin/pip install -r requirements.txt

RUN useradd -m -d /home/ctfuser -s /bin/bash ctfuser

RUN chown -R ctfuser:ctfuser /app && \
    chmod -R 550 /app

USER ctfuser

CMD ["/opt/ffam/bin/python","-B" ,"server.py"]

EXPOSE 10000