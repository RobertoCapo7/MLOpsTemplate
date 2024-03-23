# Template MLOps
The following repository contains a template for Digital Health projects. Through the use of Cookiecutter, the aim is to provide a standardized structure that facilitates the creation of new projects. The developed template includes MLOps practices, ensuring effective management of the Machine Learning model lifecycle. The main goal is to make the creation of Digital Health projects accessible even to those who may not be experts in MLOps, providing a flexible framework that adapts to various needs.

## Repository structure
```
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
│
# First use of the template
## Requirements to use the template
### Python
SciPy 1.9, a dependency of the template, supports Python versions 3.8 through 3.11.

   You can check the installed version of Python using the following command in the terminal:
 ``` bash
 python --version
```
 Building SciPy requires compilers for C, C++, Fortran, as well as the python transpilers Cython and Pythran:
  ``` bash
 Debian/Ubuntu: "sudo apt build-dep scipy"
 Fedora: "sudo dnf builddep scipy"
 CentOS/RHEL: "sudo yum-builddep scipy"
 Arch: "sudo pacman -S gcc-fortran openblas"
 ```
 ``` bash
 MacOS: "xcode-select --install"
  ```
 ``` bash
 Windows: "MinGW (Basic Setup -> Select all package and install)"
 ```
 ### Make
 Install make:
  ``` bash
 Debian/Ubuntu: "sudo apt install make"
 Fedora: "sudo dnf install make"
 CentOS/RHEL: "sudo yum install make"
 Arch: "sudo pacman -S make"
 ```
  ``` bash
 MacOS: Install homebrew from "https://brew.sh"
        "brew install make"
  ```
   ``` bash
 Windows: Install Chocolatey from "https://chocolatey.org/install"
            "choco install make"
 ```
 ### Cookiecutter
 Cookiecutter Python Package >= 2.5.0: To install it, you need to use this command in the terminal:
 ``` bash
 pip install cookiecutter
```
## Creating a new project
To create a new project, you need to use the following command in the terminal:
 ``` bash
 cookiecutter https://github.com/collab-uniba/MLOpsTemplate
```
or
 ``` bash
 python3 -m cookiecutter https://github.com/collab-uniba/MLOpsTemplate
```
At the end of the template download, for the creation of the project directory, Cookiecutter will prompt for some input information. Please respond to all Cookiecutter prompts and make sure not to leave any variable empty.
## Creation and installation of requirements in the virtual environment 'venv'
To create the virtual environment and install the requirements, follow these steps:
1. Open the terminal in the directory created by Cookiecutter.
2. Run the following commands:
 ``` bash
 make virtualenv
 make install (make update
```
## Configure Git credentials, initialize GitHub repository, and configure DVC [Optional]
To set up Git credentials, using the username and password provided as input to Cookiecutter, initialize a GitHub repository with the URL provided as input to Cookiecutter, and configure DVC, follow these steps:
1. Open the terminal in the main directory.
2. Run the following command:
 ``` bash
  make setup_versioning
 ```
If you are using Windows, use **Git Bash** to execute the command.
# Tools usage with Make
## MLFlow
### Start MLFlow UI
To start the local server hosting the MLFlow user interface, type the following command in the terminal:
 ``` bash
  make start_tracking
 ```
Once the server is started, open your browser and connect to the following URL:
``` bash
  http://localhost:8080
 ```
To stop monitoring, press CTRL + C.
### Configure MLFlow UI server port
In case of issues regarding the port used by the local MLFlow UI server, it is possible to change it in the Makefile.
### Quality Assurance Tests
In this template, quality assurance tools have been used. To start ruff, pynblint, bandit, mypy, and pytest, type the following command in the terminal:
``` bash
  make start_QA
 ```