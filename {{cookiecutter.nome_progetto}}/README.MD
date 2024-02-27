# {{cookiecutter.nome_progetto}}

**Autore**: {{cookiecutter.autore_progetto}},

**Email**: {{cookiecutter.email_autore}}

**Versione**: {{cookiecutter.versione_progetto}}

{{cookiecutter.descrizione_progetto}}

## Struttura della directory
```
├── conf               <- Directory con file di configurazione.
├── data
│   ├── external       <- Dati provenienti da fonti terze.
│   ├── interim        <- Dati intermedi trasformati.
│   ├── processed      <- set di dati finali, canonici per la modellazione.
│   └── raw            <- Dump dei dati originale e immutabile.
├── docs               <- Directory per documentazione.
├── models             <- Modelli addestrati e serializzati, previsioni di modelli o riepiloghi di modelli.
├── notebooks          <- Directory con Jupyter notebooks.
├── references         <- Directory contenente le referenze del progetto.
├── reports            <- Report generati HTML, PDF, LaTeX, etc.
│   └── figures        <- Grafici e figure generati da utilizzare nei report.
├── src                <- Codice sorgente del progetto.
│   ├── data           <- Script per scaricare o generare dati.  
│   ├── features       <- Script per trasformare i dati grezzi in features.
│   ├── models         <- Script per addestrare e utilizzare i modelli.        
│   └── visualization  <- Script per creare visualizzazioni.
├── Makefile           <- Makefile con comando `make install_requirements`.
├── README.md          <- File markdown del progetto creato.
├── requirements.txt   <- File txt contenente tutti i requisiti da installare in venv.
```