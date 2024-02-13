import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, \
    AdaBoostClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import PrecisionRecallDisplay, RocCurveDisplay, \
    confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from stop_words import get_stop_words
import pandas as pd
from matplotlib import pyplot as plt
import warnings
import mlflow

path_dataset = "{{cookiecutter.nome_progetto}}/dataset/GialloZafferanoDataset.csv"

warnings.filterwarnings("ignore")

with mlflow.start_run() as run:
    print("run_id: {}".format(run.info.run_id))
    print("experiment_id: {}".format(run.info.experiment_id))
    print("status: {}".format(run.info.status))
    print("start_time: {}".format(run.info.start_time))
    print("lifecycle_stage: {}".format(run.info.lifecycle_stage))
    
    df = pd.read_csv(path_dataset)

    vectorizer = CountVectorizer(stop_words=get_stop_words('it'))
    df_testo_vettorizzato = pd.DataFrame(vectorizer.fit_transform(df['Ingredienti']).toarray(),
                                        columns=vectorizer.get_feature_names_out())
    df_testo_vettorizzato2 = pd.DataFrame(vectorizer.fit_transform(df['Descrizione']).toarray(),
                                        columns=vectorizer.get_feature_names_out())

    colonne = ['Grassi(g)', 'Carboidrati(g)', 'Proteine(g)', 'Energia(kcal)', 'GrassiSaturi(g)', 'Fibre(g)',
            'Colesterolo(g)', 'Sodio(g)']

    X = pd.concat([df[colonne], df_testo_vettorizzato], axis=1)
    y = df['Vegano']

    models = {
        'Logistic Regression': (LogisticRegression(), {'C': [0.001, 0.01, 0.1, 1, 10, 100]}),
        'Decision Tree': (DecisionTreeClassifier(), {'max_depth': [None, 5, 10, 15], 'min_samples_split': [2, 5, 10]}),
        'RandomForestClassifier': (RandomForestClassifier(), {'n_estimators': [50, 100], 'max_depth': [None, 5, 10]}),
        'GrandientBoostingClassifier': (GradientBoostingClassifier(), {'n_estimators': [50, 100], 'learning_rate': [0.01, 0.1, 0.2]}),
        'AdaBoostClassifier': (AdaBoostClassifier(), {'n_estimators': [50, 100], 'learning_rate': [0.01, 0.1, 0.2]})
    }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    for model_name, (model, params) in models.items():
        print("Valutazione modello", model_name)
        
        kfold = KFold(n_splits=5, shuffle=True, random_state=42)
        grid_search = GridSearchCV(model, params, cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)

        best_params = grid_search.best_params_

        best_model = grid_search.best_estimator_

        test_accuracy = best_model.score(X_test, y_test)
        y_pred = best_model.predict(X_test)

        fig_cm = plt.figure()
        cm = confusion_matrix(y_test, y_pred, labels=best_model.classes_)
        disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=plt.gca())
        disp.plot()
        mlflow.log_figure(fig_cm, model_name + "ConfusionMatrix.png")
        
        fig_rc = plt.figure()
        rc = RocCurveDisplay.from_predictions(y_test, y_pred, ax=plt.gca())
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        mlflow.log_figure(fig_rc, model_name + "RocCurve.png")
                
        fig_pr = plt.figure()
        pr = PrecisionRecallDisplay.from_predictions(y_test, y_pred, ax=plt.gca())
        mlflow.log_figure(fig_pr, model_name + "PrecisionRecallCurve.png")

        mlflow.sklearn.log_model(sk_model=best_model, artifact_path=model_name)
        mlflow.log_param(model_name + " best_param", best_params)
        mlflow.log_metric(model_name + " accuratezza", test_accuracy)
    
print("end_time: {}".format(run.info.end_time))

