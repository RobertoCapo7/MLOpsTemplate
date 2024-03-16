# Makefile
SHELL = /bin/bash

.ONESHELL:
virtualenv:
	python3 -m venv venv
install:
	source venv/bin/activate && \
	python3 -m pip install -r requirements.txt
start_tracking:
	@echo "Start monitoring..."
	mlflow server --host 127.0.0.1 --port 8080 --backend-store-uri src/models/mlruns
	mlflow ui
start_QA:
	@echo "Start check Quality Assurance..."
	ruff check .
	ruff format .
	pynblint notebooks
	bandit -r src
	mypy src
	pytest test/