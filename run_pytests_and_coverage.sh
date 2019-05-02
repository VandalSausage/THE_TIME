#!/bin/bash

echo "######## RUNNING PYTESTS"
coverage run --omit /venv/* --source='.' -m pytest

echo "######## GENERATING COVERAGE REPORT"
coverage html

echo "######## CHECK HTML REPORT at /THE_TIME/htmlcov/index.html"
