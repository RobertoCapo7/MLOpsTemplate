---
# Consulta il seguente link per i metadati che possono essere aggiunti: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
# Documentazione/Guida: https://huggingface.co/docs/hub/datasets-cards
---

# Dataset Card for {{ pretty_name | default("Dataset Name", true) }}

<!-- Fornisci un breve riassunto del dataset. -->

{{ dataset_summary | default("", true) }}

## Dataset Details

### Dataset Description

<!-- Fornisci un riassunto più dettagliato su cosa tratta il dataset. -->

{{ dataset_description | default("", true) }}

- **Curated by:** {{ curators | default("[{{cookiecutter.autore_progetto}}]", true)}}
- **Funded by [optional]:** {{ funded_by | default("[More Information Needed]", true)}}
- **Shared by [optional]:** {{ shared_by | default("[More Information Needed]", true)}}
- **Language(s) (NLP):** {{ language | default("[More Information Needed]", true)}}
- **License:** {{ license | default("[More Information Needed]", true)}}

### Dataset Sources [optional]

<!-- Sezione contenente i link basilari per il dataset. -->

- **Repository:** {{ repo | default("[{{cookiecutter.repository_url}}]", true)}}
- **Paper [optional]:** {{ paper | default("[More Information Needed]", true)}}
- **Demo [optional]:** {{ demo | default("[More Information Needed]", true)}}

## Uses

<!-- Questa sezione è dedicata alle domande su come si utilizza il dataset. -->

### Direct Use

<!-- Questa sezione descrive i casi d'uso adatti per il set di dati. -->

{{ direct_use | default("[More Information Needed]", true)}}

### Out-of-Scope Use

<!-- Questa sezione affronta l'uso improprio, dannoso e gli usi per i quali il dataset non funzionerà bene. -->

{{ out_of_scope_use | default("[More Information Needed]", true)}}

## Dataset Structure

<!-- Questa sezione fornisce una descrizione dei campi del dataset e informazioni aggiuntive sulla struttura del dataset, come i criteri utilizzati per creare le suddivisioni, le relazioni tra i data points, ecc. -->

{{ dataset_structure | default("[More Information Needed]", true)}}

## Dataset Creation

### Curation Rationale

<!-- Inserire le motivazioni per la creazione di questo dataset. -->

{{ curation_rationale_section | default("[More Information Needed]", true)}}

### Source Data

<!-- Questa sezione descrive i dati di origine (ad esempio, testi e titoli di notizie, post sui social media, frasi tradotte, ...). -->

#### Data Collection and Processing

<!-- Questa sezione descrive il processo di raccolta e elaborazione dei dati, come i criteri di selezione dei dati, i metodi di filtraggio e normalizzazione, gli strumenti e le librerie utilizzate, ecc. -->

{{ data_collection_and_processing_section | default("[More Information Needed]", true)}}

#### Who are the source data producers?

<!-- Questa sezione descrive le persone o i sistemi che originariamente hanno creato i dati. Dovrebbe includere anche informazioni demografiche o di identità autodichiarate per i creatori dei dati di origine, se tali informazioni sono disponibili. -->

{{ source_data_producers_section | default("[More Information Needed]", true)}}

### Annotations [optional]

<!-- Se il set di dati contiene annotazioni che non fanno parte della raccolta dati iniziale, utilizzare questa sezione per descriverle. -->

#### Annotation process

<!-- Questa sezione descrive il processo di annotazione come gli strumenti di annotazione utilizzati nel processo, la quantità di dati annotati, le linee guida per l'annotazione fornite agli annotatori, le statistiche degli interannotatori, la convalida delle annotazioni, ecc. -->

{{ annotation_process_section | default("[More Information Needed]", true)}}

#### Who are the annotators?

<!-- Questa sezione descrive le persone o i sistemi che hanno creato le annotazioni. -->

{{ who_are_annotators_section | default("[More Information Needed]", true)}}

#### Personal and Sensitive Information

<!-- Indicare se il set di dati contiene dati che potrebbero essere considerati personali, sensibili o privati (ad esempio, dati che rivelano indirizzi, nomi o alias identificabili in modo univoco, origini razziali o etniche, orientamenti sessuali, credenze religiose, opinioni politiche, dati finanziari o sanitari, ecc. .). Se sono stati compiuti sforzi per anonimizzare i dati, descrivere il processo di anonimizzazione. -->

{{ personal_and_sensitive_information | default("[More Information Needed]", true)}}

## Bias, Risks, and Limitations

<!-- Questa sezione è destinata alle limitazioni tecniche e a quelle socio-tecniche. -->

{{ bias_risks_limitations | default("[More Information Needed]", true)}}

### Recommendations

<!-- Questa sezione ha lo scopo di fornire raccomandazioni riguardanti il bias, il rischio e le limitazioni tecniche. -->

{{ bias_recommendations | default("Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.", true)}}

## Citation [optional]

<!-- In questa sezione vanno inseriti gli articoli o dei post di blog che introducono il dataset, le informazioni APA e Bibtex. -->

**BibTeX:**

{{ citation_bibtex | default("[More Information Needed]", true)}}

**APA:**

{{ citation_apa | default("[More Information Needed]", true)}}

## Glossary [optional]

<!-- Includere in questa sezione termini e calcoli che possono aiutare i lettori a comprendere il modello o la scheda del modello. -->

{{ glossary | default("[More Information Needed]", true)}}

## More Information [optional]

{{ more_information | default("[More Information Needed]", true)}}

## Dataset Card Authors [optional]

{{ dataset_card_authors | default("[{{cookiecutter.autore_progetto}}]", true)}}

## Dataset Card Contact

{{ dataset_card_contact | default("[{{cookiecutter.email_autore}}]", true)}}
