#!/bin/sh

gunicorn api:app -b 0.0.0.0:8001