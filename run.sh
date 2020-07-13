#!/usr/bin/env bash

source venv/bin/activate

export FLASK_ENV=development
export FLASK_APP=app_runner.py

flask run