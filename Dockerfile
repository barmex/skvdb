FROM python:3.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /app
COPY api.py /app
COPY db.py /app
COPY gunicorn-starter.sh /app
ENTRYPOINT ["./gunicorn-starter.sh"]