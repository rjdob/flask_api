from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from prometheus_client import start_http_server, Counter, generate_latest

app = Flask(__name__)


model = joblib.load('data/modele_sklearn.pkl')

# Créer un compteur (counter) Prometheus pour suivre le nombre de requêtes
REQUEST_COUNT = Counter("http_requests_total", "Nombre total de consultation du site")
PREDICT_COUNT = Counter("nb_predicts", "Nombre d'appels à la prédiction")
TEST_COUNT = Counter("nb_tests", "Nombre d'appels au test")

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    PREDICT_COUNT.inc()
    # Récupérer les données de la requête
    age = float(request.form['Age'])
    account_manager = float(request.form['Account_Manager'])
    years = float(request.form['Years'])
    num_sites = float(request.form['Num_Sites'])
    # Convertir les données en format numpy array
    features = np.array([[age, account_manager, years, num_sites]])
    # Faire la prédiction
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/test', methods=['GET'])
def test():
    TEST_COUNT.inc()
    return jsonify({'retour': 'ok'})

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    start_http_server(8000)
    app.run(debug=True, host='0.0.0.0', port=5000)