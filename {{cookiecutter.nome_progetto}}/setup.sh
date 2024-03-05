#!/bin/sh

configurazione_git="{{cookiecutter.configurazione_git}}"
repository_url="{{cookiecutter.repository_url}}"
autore="{{cookiecutter.autore_progetto}}"
email_autore="{{cookiecutter.email_autore}}"
data_dir="{{cookiecutter.data_dir}}"
data_directory_name="{{cookiecutter.data_directory_name}}"
configurazione_DVC="{{cookiecutter.configurazione_DVC}}"

check_empty() {
    var_name=$1
    eval var_value=\$$var_name

    if [ -z "$var_value" ]; then
        echo "Errore! La variabile $var_name è vuota!"
        exit 1

    fi
}

for var in configurazione_git configurazione_DVC repository_url autore email_autore data_dir data_directory_name; do
    check_empty $var
done

git init

if [ "$configurazione_git" = "si" ];
    then

    git config user.name "{{cookiecutter.autore_progetto}}"
    git config user.email "{{cookiecutter.email_autore}}"

    git remote add origin {{cookiecutter.repository_url}}
    git fetch
    git pull origin master
    mv {{cookiecutter.data_directory_name}} {{cookiecutter.data_dir}}
    git add .
    git commit -m 'initializing from cookiecutter'
    git push -u origin master
    git branch -M master feature/initialize_template
    git branch --remotes --delete  origin/master
    git push origin HEAD
    fi

if [ "$configurazione_DVC" = "si" ];
    then
    dvc init
    touch dvc.yaml
    fi