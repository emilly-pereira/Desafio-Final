import unittest
from app import app
import werkzeug
import json

# Patch temporário para adicionar o atributo '__version__' em werkzeug 
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_home(self):
        # valida que rota raiz responde com a mensagem e status 200
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})
    
    #Valida se a rota /items retorna conteúdo JSON.
    def test_items_content_type(self):
        resp = self.client.get('/items')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('application/json', resp.content_type)

    def test_swagger_ui_available(self):
        resp = self.client.get('/swagger/')
    # Verifica se a interface Swagger está funcinando
        self.assertIn(resp.status_code, [200, 302])(resp.status_code, 401)

    def test_items_response_is_dict(self):
        # Verifica se a resposta de /items é um JSON em formato dict
        resp = self.client.get('/items')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json, dict)

        headers = {
            'Authorization': f'Bearer {token}'
        }
        resp = self.client.get('/protected', headers=headers)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, {"message": "Protected route"})

if __name__ == '__main__':
    unittest.main()