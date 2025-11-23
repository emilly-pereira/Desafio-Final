import unittest
from app import app
import werkzeug
import json

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

def test_saudacao(self):
    # valida que rota /saudacao responde com a mensagem e status 200
    response = self.client.get('/saudacao')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, {"mensagem": "Olá, bem-vindo ao Desafio Final!"})

    
    #Verifica estrutura dos itens (/items)
def test_items_structure(self):
    resp = self.client.get('/items')
    self.assertEqual(resp.status_code, 200)
    data = resp.get_json()

    # valida se existe "items"
    self.assertIn('items', data)
    items = data['items']

    for item in items:
            self.assertIn('id', item)
            self.assertIn('name', item)
            self.assertIsInstance(item['id'], int)
            self.assertIsInstance(item['name'], str)

    # Verifica se a interface Swagger está funcinando 
def test_swagger_ui_available(self): 
    resp = self.client.get('/swagger/')
    self.assertIn(resp.status_code, [200, 302])(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()