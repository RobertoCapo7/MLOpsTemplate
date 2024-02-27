# Template MLOps
_Il seguente repository contiene un template per progetti di Digital Health. Attraverso l'utilizzo di Cookiecutter, si mira a fornire una struttura standardizzata che faciliti la creazione di nuovi progetti. Il template sviluppato include le pratiche di MLOps, garantendo la gestione efficace del ciclo di vita dei modelli di Machine Learning. L’obiettivo principale è quello di rendere accessibile la creazione di progetti di Digital Health anche a coloro che potrebbero non essere esperti in MLOps, fornendo un framework flessibile che si adatta a diverse esigenze._

## Struttura della directory
```
├── {{cookiecutter.nome_progetto}}    <- Directory principale del progetto.
│    ├── conf               <- Directory con file di configurazione.
│    ├── data
│    │   ├── external       <- Dati provenienti da fonti terze.
│    │   ├── interim        <- Dati intermedi trasformati.
│    │   ├── processed      <- set di dati finali, canonici per la modellazione.
│    │   └── raw            <- Dump dei dati originale e immutabile.
│    ├── docs               <- Directory per documentazione.
│    ├── models             <- Modelli addestrati e serializzati, previsioni di modelli o riepiloghi di modelli.
│    ├── notebooks          <- Directory con Jupyter notebooks.
│    ├── references         <- Directory contenente le referenze del progetto.
│    ├── reports            <- Report generati HTML, PDF, LaTeX, etc.
│    │   └── figures        <- Grafici e figure generati da utilizzare nei report.
│    ├── src                <- Codice sorgente del progetto.
│    │   ├── data           <- Script per scaricare o generare dati.  
│    │   ├── features       <- Script per trasformare i dati grezzi in features.
│    │   ├── models         <- Script per addestrare e utilizzare i modelli.        
│    │   └── visualization  <- Script per creare visualizzazioni.
│    ├── Makefile           <- Makefile con comando `make install_requirements`.
│    ├── README.md          <- File markdown del progetto creato.
│    ├── requirements.txt   <- File txt contenente tutti i requisiti da installare in venv.
├── cookiecutter.json     <- File di configurazione Cookiecutter.
├── README.md             <- File markdown per gli sviluppatori che utilizeranno il template.
```

# Primo utilizzo del template
## Requisiti per utilizzare il template
 - Python 3.10+
 - Cookiecutter Python Package >= 2.5.0: Per poterlo installare bisogna utilizzare questo comando da terminale:
 ``` bash
 pip install cookiecutter
```
## Creazione di un nuovo progetto
Per poter creare un nuovo progetto bisogna utilizzare il seguente comando da terminale:
 ``` bash
 cookiecutter https://github.com/RobertoCapo7/MLOpsTemplate/  
```
Al termine del download del template, per la creazione della directory del progetto, cookiecutter richiederà alcune informazioni in input. Rispondere a tutte le richieste di cookiecutter.
## Creazione dell'ambiente virtuale venv
Per la creazione dell'ambiente virtuale e l'installazione dei requisiti bisogna seguire i seguenti passi:
1. Aprire il terminale nella directory creata da cookiecutter
2. Eseguire il seguente comando:
 ``` bash
 make install_requirements
```
## [Opzionale] Configurazione Git
Per poter configurare git con il nome utente e la password date in input a cookiecutter bisogna seguire i seguenti passi:
1. Aprire il terminale nella directory conf
2. Eseguire il seguente comando:
 ``` bash
 ./git_configuration.sh
 ```
 In caso di problemi, rendere lo script eseguibile:
 ``` bash
  chmod +x git_configuration.sh 
 ```

# Utilizzo Tools
## MLFlow
### Avviare MLFlow UI
Per poter avviare il server locale che ospita l'interfaccia utente di MLFlow digitare il seguente comando da terminale:
 ``` bash
  mlflow ui
 ```
Una volta avviato il server, aprire il browser e connettersi al seguente URL:
``` bash
  http://localhost:8080
 ```
### Configurare porta server MLFlow UI
In caso di problemi inerenti alla porta utilizzata dal server locale mlflow ui è possibile cambiarla dallo script python 'config.py' contenuto nella directory 'conf'.
