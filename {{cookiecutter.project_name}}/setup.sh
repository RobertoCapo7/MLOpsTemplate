#!/bin/sh

git_configuration="{{cookiecutter.git_configuration}}"
repository_url="{{cookiecutter.repository_url}}"
author_name="{{cookiecutter.author_name}}"
author_email="{{cookiecutter.author_email}}"
data_dir="{{cookiecutter.data_dir}}"
data_dir_name="{{cookiecutter.data_directory_name}}"
DVC_configuration="{{cookiecutter.DVC_configuration}}"

check_empty() {
    var_name=$1
    eval var_value=\$$var_name

    if [ -z "$var_value" ]; then
        echo "Error! The variable $var_name is empty!"
        exit 1

    fi
}

for var in git_configuration DVC_configuration repository_url author_name author_email data_dir data_dir_name; do
    check_empty $var
done

git init

if [ "$git_configuration" = "yes" ];
    then
    git config user.name "{{cookiecutter.author_name}}"
    git config user.email "{{cookiecutter.author_email}}"
    git remote add origin {{cookiecutter.repository_url}}
    git fetch
    git pull origin master
    mv {{cookiecutter.data_dir_name}} {{cookiecutter.data_dir}}
    git add .
    git commit -m 'initializing from cookiecutter'
    git push -u origin master
    git branch -M master feature/initialize_template
    git branch --remotes --delete  origin/master
    git push origin HEAD
    fi

if [ "$DVC_configuration" = "yes" ];
    then
    dvc init
    touch dvc.yaml
    fi