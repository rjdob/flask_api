import unittest, json
from app import app

class FlaskTestCase(unittest.TestCase):
    
    # Setup avant chaque test : crée un client de test pour envoyer des requêtes à l'application Flask
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # Test pour la route "/test" qui renvoie "ok"
    def test_test_endpoint(self):
        response = self.client.get('/test')
        print("Response", response.data)
        self.assertEqual(response.status_code, 200)  # Vérifie que le code de statut est 200        
        self.assertEqual(response.data, b'{"retour":"ok"}\n')  # Vérifie que la réponse est bien "ok"

    # Test pour la route "/predict"
    def test_predict_endpoint(self):
        # Envoie une requête POST avec des données de test
        response = self.client.post('/predict', data={
            'Age': '25',
            'Account_Manager': '0',
            'Years': '5',
            'Num_Sites': '3'
        })
        # Vérifie que la réponse a un code de statut 200
        self.assertEqual(response.status_code, 200)
        
        # Assure-toi que la réponse est en JSON et contient une clé 'prediction'
        response_json = response.get_json()
        self.assertIn('prediction', response_json)

if __name__ == '__main__':
    unittest.main()
