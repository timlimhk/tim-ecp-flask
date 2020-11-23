import requests
import pytest
import unittest
import sys

def assert_exit(condition, err_message):
    try:
        assert condition
    except AssertionError:
        sys.exit(err_message)

class BasicE2ETestCase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def check_unitRemote(self,unitRemote):
       self.unitRemote=unitRemote
       if self.unitRemote == None :
           assert_exit(False, "--unitRemote http://{hostname}:{port} is not specified with pytest run")
       else:
           pass
    def test_get_home_check_status_code_equals_200(self):
       response = requests.get(self.unitRemote)
       assert response.status_code == 200
    def test_get_info_check_content_type_equals_json(self):
       response = requests.get(self.unitRemote + "/info")
       assert response.headers["Content-Type"] == "application/json"
    def test_get_info_check_appname(self):
        response = requests.get(self.unitRemote + "/info")
        response_body = response.json()
        assert response_body["Service_name"] == "tim-ecp"
    def test_get_missing_check_status_code_equals_404(self):
        response = requests.get(self.unitRemote + "/missing")
        assert response.status_code == 404
