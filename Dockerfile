FROM python:3.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /app
COPY api.py /app
COPY db.py /app
ENTRYPOINT ["gunicorn"]
CMD ["--chdir app api:app -b 0.0.0.0:8001"]