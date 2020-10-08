from server import app
import unittest

class EndpointsTests(unittest.TestCase):
    ''' Unit testcases for REST APIs '''

    def test_index_returns_200(self):
        request, response = app.test_client.get('/')
        assert response.status == 200

    def test_index_returns_hello_world(self):
        request, response = app.test_client.get('/')
        body = response.json
        assert body['hello'] == "world"

if __name__ == '__main__':
    unittest.main()
