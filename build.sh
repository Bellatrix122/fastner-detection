#!/usr/bin/env bash
# Render runs this automatically on every deploy

set -o errexit   # stop if any command fails

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate