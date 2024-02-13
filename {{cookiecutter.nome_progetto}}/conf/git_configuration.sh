#!/bin/sh

configurazione_git="{{cookiecutter.configurazione_git}}"
repository_url="{{cookiecutter.repository_url}}"
author="{{cookiecutter.autore_progetto}}"
author_email="{{cookiecutter.email_autore}}"
data_dir="{{cookiecutter.data_dir}}"
data_directory_name="{{cookiecutter.data_directory_name}}"

# Function to check if a variable is empty
check_empty() {
    var_name=$1
    eval var_value=\$$var_name

    if [ -z "$var_value" ]; then
        echo "$var_name is empty"
        exit 1
    else
        echo "$var_name has the value: $var_value"
    fi
}

# List your variables
for var in configurazione_git repository_url author author_email data_dir data_directory_name; do
    check_empty $var
done

if [ "$configurazione_git" = "si" ];
    then
    git init

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

