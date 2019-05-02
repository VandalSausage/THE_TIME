#!/bin/bash

echo "######## RUNNING BEHAVE TESTS"
coverage run --omit /venv/* --source='.' -m behave

echo "######## GENERATING COVERAGE REPORT"
coverage html

echo "######## CHECK HTML REPORT at /THE_TIME/htmlcov/index.html"
