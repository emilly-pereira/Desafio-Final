import unittest
from app import app
import werkzeug

# workaround (se realmente necessário em seu ambiente)
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
        self.assertEqual(response.get_json(), {"mensagem": "Olá, bem-vindo ao Desafio Final!"})

    def test_items_structure(self):
        # Verifica estrutura dos itens (/items)
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

    def test_swagger_ui_available(self):
        # Verifica se a interface Swagger está funcionando
        resp = self.client.get('/swagger/')
        # aceitar 200 (OK), 302 (redirect) ou 401 (se existir proteção)
        self.assertIn(resp.status_code, [200, 302, 401])

if __name__ == '__main__':
    unittest.main()
