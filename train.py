from sklearn.linear_model import LogisticRegression
import pandas as pd
import joblib
import numpy as np


dataset = pd.read_csv("data/customer_churn.csv")
X = dataset[['Age', 'Account_Manager', 'Years', 'Num_Sites']]
y = dataset['Churn']

# On crée l'objet de régression
regr = LogisticRegression()
# On entraîne le modèle sur notre base d'apprentissage
regr.fit(X, y)


joblib.dump(regr, 'data/modele_sklearn.pkl')

model = joblib.load('data/modele_sklearn.pkl')