#!/usr/bin/env bash

# Create VirtualEnv
if [[ ! -d "venv" ]]; then
    python3 -m venv venv
fi

# Install dependencies
source venv/bin/activate
pip install -r requirements.txt
deactivate