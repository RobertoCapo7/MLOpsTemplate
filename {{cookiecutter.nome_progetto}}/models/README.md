---
# Consulta il seguente link per i metadati che possono essere aggiunti: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Documentazione/Guida: https://huggingface.co/docs/hub/model-cards
{{ card_data }}
---

# Model Card for {{ model_id | default("Model ID", true) }}

<!-- Fornisci un breve riassunto di cosa è/cosa fa il modello. -->

{{ model_summary | default("", true) }}

## Model Details

### Model Description

<!-- Fornisci un riassunti più lungo di cosa è/cosa fa il modello. -->

{{ model_description | default("", true) }}

- **Developed by:** {{ developers | default("[{{cookiecutter.autore_progetto}}]", true)}}
- **Funded by [optional]:** {{ funded_by | default("[More Information Needed]", true)}}
- **Shared by [optional]:** {{ shared_by | default("[More Information Needed]", true)}}
- **Model type:** {{ model_type | default("[More Information Needed]", true)}}
- **Language(s) (NLP):** {{ language | default("[More Information Needed]", true)}}
- **License:** {{ license | default("[More Information Needed]", true)}}
- **Finetuned from model [optional]:** {{ base_model | default("[More Information Needed]", true)}}

### Model Sources [optional]

<!-- Sezione contenente i link basilari per il modello. -->

- **Repository:** {{ repo | default("[{{cookiecutter.repository_url}}]", true)}}
- **Paper [optional]:** {{ paper | default("[More Information Needed]", true)}}
- **Demo [optional]:** {{ demo | default("[More Information Needed]", true)}}

## Uses

<!-- Questa sezione è dedicata alle domande su come si utilizza il modello, includendo gli utenti che lo utilizzeranno e quelli che sono interessati ad esso. -->

### Direct Use

<!-- Questa sezione riguarda l'utilizzo del modello senza fine-tuning o senza integrazioni in un ecosystem/app più grande. -->

{{ direct_use | default("[More Information Needed]", true)}}

### Downstream Use [optional]

<!-- Questa sezione riguarda l'utilizzo del modello quando è fine-tuning per un task, o quando è integrato in un ecosystem/app più grande. -->

{{ downstream_use | default("[More Information Needed]", true)}}

### Out-of-Scope Use

<!-- Questa sezione affronta l'uso improprio, dannoso e gli usi per i quali il modello non funzionerà bene.  -->

{{ out_of_scope_use | default("[More Information Needed]", true)}}

## Bias, Risks, and Limitations

<!-- Questa sezione è destinata alle limitazioni tecniche e a quelle socio-tecniche. -->

{{ bias_risks_limitations | default("[More Information Needed]", true)}}

### Recommendations

<!-- Questa sezione ha lo scopo di fornire raccomandazioni riguardanti il bias, il rischio e le limitazioni tecniche. -->

{{ bias_recommendations | default("Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.", true)}}

## How to Get Started with the Model

Use the code below to get started with the model.

{{ get_started_code | default("[More Information Needed]", true)}}

## Training Details

### Training Data

<!-- Questa sezione è collegata al dataset card. Descrivere in breve in cosa consistono i dati di addestramento, fornire una documentazione relativa alla fase di pre-processing dei dati o di un ulteriore filtraggio dati. -->

{{ training_data | default("[More Information Needed]", true)}}

### Training Procedure

<!-- Questa sezione è dedicata alle specifiche tecniche. -->

#### Preprocessing [optional]

{{ preprocessing | default("[More Information Needed]", true)}}


#### Training Hyperparameters

- **Training regime:** {{ training_regime | default("[More Information Needed]", true)}} <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- Questa sezione contiene le informazioni sulle capacità, tempo di inizio/fine, le dimensioni del checkpoint (se rilevanti), etc. -->

{{ speeds_sizes_times | default("[More Information Needed]", true)}}

## Evaluation

<!-- Questa sezione descrive i protocolli di valutazione e fornisce i risultati. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- Questa sezione dovrebbe essere collegata a una Scheda dei Dati se possibile. -->

{{ testing_data | default("[More Information Needed]", true)}}

#### Factors

<!-- Questa sezione contiene gli elementi per cui la valutazione viene scomposta, ad esempio, sottoinsiemi di popolazioni o domini -->

{{ testing_factors | default("[More Information Needed]", true)}}

#### Metrics

<!-- Questa sezione contiene le metriche di valutazione utilizzate, idealmente con una descrizione del perché vengono utilizzate -->

{{ testing_metrics | default("[More Information Needed]", true)}}

### Results

{{ results | default("[More Information Needed]", true)}}

#### Summary

{{ results_summary | default("", true) }}

## Model Examination [optional]

<!-- In questa sezione vanno inseriti i lavori sull'interpretabilità rilevanti per il modello. -->

{{ model_examination | default("[More Information Needed]", true)}}

## Environmental Impact

<!-- In questa sezione vanno inserite le emissioni totali (in grammi di CO2eq) e considerazioni aggiuntive, come il consumo di elettricità. Modifica il testo riportato in seguito a seconda delle necessità. -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** {{ hardware_type | default("[More Information Needed]", true)}}
- **Hours used:** {{ hours_used | default("[More Information Needed]", true)}}
- **Cloud Provider:** {{ cloud_provider | default("[More Information Needed]", true)}}
- **Compute Region:** {{ cloud_region | default("[More Information Needed]", true)}}
- **Carbon Emitted:** {{ co2_emitted | default("[More Information Needed]", true)}}

## Technical Specifications [optional]

### Model Architecture and Objective

{{ model_specs | default("[More Information Needed]", true)}}

### Compute Infrastructure

{{ compute_infrastructure | default("[More Information Needed]", true)}}

#### Hardware

{{ hardware_requirements | default("[More Information Needed]", true)}}

#### Software

{{ software | default("[More Information Needed]", true)}}

## Citation [optional]

<!-- In questa sezione vanno inseriti gli articoli o dei post di blog che introducono il modello, le informazioni APA e Bibtex. -->

**BibTeX:**

{{ citation_bibtex | default("[More Information Needed]", true)}}

**APA:**

{{ citation_apa | default("[More Information Needed]", true)}}

## Glossary [optional]

<!-- Includere in questa sezione termini e calcoli che possono aiutare i lettori a comprendere il modello o la scheda del modello -->

{{ glossary | default("[More Information Needed]", true)}}

## More Information [optional]

{{ more_information | default("[More Information Needed]", true)}}

## Model Card Authors [optional]

{{ model_card_authors | default("[{{cookiecutter.autore_progetto}}]", true)}}

## Model Card Contact

{{ model_card_contact | default("[{{cookiecutter.email_autore}}]", true)}}
