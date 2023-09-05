#!/bin/sh

gunicorn --chdir app api:app -b 0.0.0.0:8001