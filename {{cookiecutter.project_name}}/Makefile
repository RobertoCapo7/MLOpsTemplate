SHELL = /bin/bash

git_configuration := "{{cookiecutter.git_configuration}}"
repository_url := "{{cookiecutter.repository_url}}"
author_name="{{cookiecutter.author_name}}"
author_email="{{cookiecutter.author_email}}"
data_dir="{{cookiecutter.data_dir}}"
DVC_configuration="{{cookiecutter.DVC_configuration}}"

.ONESHELL:
virtualenv:
	python3 -m venv venv
	@echo "Virtual environment created successfully"

install:
	source venv/bin/activate && \
	python3 -m pip install -r requirements.txt

update:
	source venv/bin/activate && \
	pip install --upgrade -r requirements.txt

setup:
	check_empty() { \
        var_name=$$1; \
        eval var_value=$$$$var_name; \
        if [ -z "$$var_value" ]; then \
            echo "Error! The variable $$var_name is empty!"; \
            exit 1; \
        fi; \
    }; \
    for var in git_configuration DVC_configuration repository_url author_name author_email data_dir; do \
        check_empty $$var; \
    done; \
    git init; \
    if [ "$(git_configuration)" = "yes" ]; then \
        git config user.name "{{cookiecutter.author_name}}"; \
        git config user.email "{{cookiecutter.author_email}}"; \
        git remote add origin {{cookiecutter.repository_url}}; \
        git fetch; \
        git pull origin master; \
        if [ "{{cookiecutter.data_dir}}" != "no" ]; then \
            mv {{cookiecutter.data_dir}} {{cookiecutter.project_name}}/data/raw; \
        fi; \
        git add .; \
        git commit -m 'initializing from cookiecutter'; \
        git push -u origin master; \
        git branch -M master feature/initialize_template; \
        git branch --remotes --delete  origin/master; \
        git push origin HEAD; \
    fi; \
    if [ "$(DVC_configuration)" = "yes" ]; then \
        dvc init; \
    fi

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
