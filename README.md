# Cookiecutter MLHOps

*A Cookiecutter Template for Building Production-ready ML Components in Healthcare*

![License](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)

This repository provides a **[Cookiecutter](https://www.cookiecutter.io) template** for developing ML-based software components to be integrated into digital health solutions.

The template aims to:

- **promote MLOps best practices** in the development of ML models for healthcare applications;
- **establish a standardized repository structure**, ensuring consistency across similar projects.

The template includes setup scripts and configuration files for a range of MLOps tools.
For instance, it enables robust experiment traceability and reproducibility by:

- integrating git and DVC for **code and data version control**, respectively;
- supporting **experiment tracking** and **model management** through MLFlow.

Additionally, the template incorporates a suite of **quality assurance** tools to ensure high code standards. These include static analyzers such as `ruff`, `pynblint`, `bandit`, and `mypy`.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Repository structure](#repository-structure)


## Requirements

To use this template, ensure the following tools are available on your system:

- Python
- Make
- Cookiecutter

### Python

This template is compatible with Python versions 3.8 to 3.11.

To check your Python version, use the following command:

 ``` bash
 python --version
 ```

### Make

If you do not have Make already available on your system, install it using the following commands:

- **Debian/Ubuntu**

  ``` bash
  sudo apt install make
  ```

- **MacOS**: Install homebrew from "https://brew.sh"; then:

  ``` bash
  brew install make
  ```

- **Windows**: Install Chocolatey from "https://chocolatey.org/install"; then:

  ``` bash
  choco install make
  ```

### Cookiecutter

This template is compatible with Cookiecutter version 2.5.0 or later.

Use [pipx](https://github.com/pypa/pipx) to install Cookiecutter on your system:

``` bash
pipx install cookiecutter
```

The use of pipx is [strongly recommended](https://cookiecutter.readthedocs.io/en/stable/README.html#installation). If you prefer using pip instead, then run:

```bash
python -m pip install --user cookiecutter
```


## Usage

To create a new MLOps project using this template, use Cookiecutter by running:

``` bash
cookiecutter https://github.com/collab-uniba/Cookiecutter-MLHOps
```

or

``` bash
python3 -m cookiecutter https://github.com/collab-uniba/Cookiecutter-MLHOps
```

Once the template download is complete, Cookiecutter will request input to create the project directory. Ensure you respond to all prompts and do not leave any fields blank.

### Step 1 - Create of a virtual environment and install the pre-defined project requirements

Once the project directory is created, you can set up a virtual environment and install the pre-defined project requirements.
These include the MLOps tools and quality assurance tools mentioned above.
To do so, follow these steps:

1. open the terminal in the directory created by Cookiecutter (hereafter referred to as the *'root directory'*);
2. run the Make commands:

   ``` bash
   make virtualenv
   make install
   ```

### Step 2 - Configure Git and DVC [Optional]

To initialize the Git repository, run the following make command:

``` bash
make initialize_git
```

To initialize the DVC repository, run the following make command:

``` bash
make initialize_dvc
```

**Note:** If you are using Windows, use **Git Bash** to execute this command.

At this point, you can push the repo to the code hosting platform of your choice (e.g., GithHub).
Likewise, you can assign a remote storage location for DVC.

### Step 3 - Start the development environment

#### MLFlow

The template includes a set of scripts to start the MLFlow server and track your ML experiments.

To start the local MLflow server, run:

``` bash
make start_tracking
```

Once the server starts, open your web browser and visit http://localhost:8080.

To stop the MLflow server, press `CTRL + C` in the terminal window where it was started.

**Note:** If you encounter issues with the port used by the local MLFlow UI server, you can change it in the Makefile.

### Step 4 – Quality Assurance

#### Static Analysis

This template provides quality assurance tools for evaluating Python code, including static analyzers such as `ruff`, `pynblint`, `bandit`, and `mypy`.

To perform static analysis using these tools, run the following command in the terminal:

```bash
make start_QA
```

#### Testing

To run your test suite using Pytest, run the following command:

```bash
make start_testing
```

## Repository structure

The repository structure promoted by this Cookiecutter template is freely inspired by the one offered in [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org).

```text
├── {{cookiecutter.project_name}}    <- Main project directory.
│  ├── data
│  │   ├── external       <- Data from third party sources.
│  │   ├── interim        <- Intermediate data that has been transformed.
│  │   ├── processed      <- The final, canonical data sets for modeling.
│  │   └── raw            <- The original, immutable data dump.
│  ├── docs               <- Directory for documentation.
│  ├── example            <- Directory for test scripts and src.
│  ├── models             <- Trained and serialized models, model predictions, or model summaries.
│  ├── notebooks          <- Directory with Jupyter notebooks.
│  ├── references         <- Directory containing project references.
│  ├── reports            <- Generated HTML, PDF, LaTeX, etc. reports.
│  │   └── figures        <- Graphs and figures generated to use in reports.
│  ├── src                <- Project source code.
│  │   ├── data           <- Scripts to download or generate data.
│  │   ├── features       <- Scripts to turn raw data into features.
│  │   ├── models         <- Scripts to train and use models.
│  │   └── visualization  <- Scripts to create visualizations.
│  ├── test               <- Project test code.
│  │   ├── data
│  │   ├── features
│  │   ├── models
│  │   └── visualization
│  ├── Makefile           <- Makefile with `make install_requirements` command.
│  ├── README.md          <- Project markdown file created.
│  ├── requirements.txt   <- Txt file containing all requirements to install in venv.
│  ├── setup.sh           <- Allows you to configure git and DVC.
├── cookiecutter.json     <- Cookiecutter configuration file.
├── README.md             <- Markdown file for developers utilizing the template.
```
