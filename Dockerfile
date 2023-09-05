FROM python:3.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /app
COPY api.py /app
COPY db.py /app
RUN chmod 755 -R /app
ENTRYPOINT ["./gunicorn-starter.sh"]