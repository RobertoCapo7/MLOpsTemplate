# Makefile
SHELL = /bin/bash

.ONESHELL:
install_requirements:
	python3 -m venv venv
	source venv/bin/activate && \
	python3 -m pip install -r requirements.txt
start_monitoring:
	@echo "Start monitoring..."
	mlflow server --host 127.0.0.1 --port 8080
	mlflow ui