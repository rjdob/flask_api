from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load('data/modele_sklearn.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
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
    return jsonify({'retour': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)