#!/bin/bash

# Run pytest tests and generate Allure results
pytest tests/login_page/ --alluredir=a

# Serve Allure report
allure serve a