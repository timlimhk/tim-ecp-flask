import unittest
import pytest  
from TimEcpFlask.app import create_app

class BasicTestCase(unittest.TestCase):
    #@pytest.fixture(autouse=True)
    #def defineApp(self):
    def setUp(self):
        app=create_app(testing=True)
        self.tester = app.test_client(self)
    def test_home(self):
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'My ECP testing site' in response.data)
    def test_other(self):
        response = self.tester.get('/info', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tim-ecp' in response.data)

if __name__ == '__main__':
    unittest.main()
