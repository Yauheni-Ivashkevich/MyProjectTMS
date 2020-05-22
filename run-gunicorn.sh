#!/usr/bin/env bash

gunicorn --config gunicorn.conf.py project.asgi:application