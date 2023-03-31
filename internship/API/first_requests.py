import requests
import json
# import jsonpath
import pytest

#nothing serious. Just first acquaintance
class TestAPI:

    def status(self):
        return self.response.status_code

    def test_get_all_authors(self):
        self.response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
        assert self.status() == 200
        jsonData = self.response.json()
        assert jsonData[4]['firstName'] == 'First Name 5'

    def test_create_author(self):
        payload = {
            'id': 777,
            'idBook': 777,
            'firstName': 'David',
            'lastName': 'Akopyan'
        }
        self.response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Authors', json=payload)
        assert self.response.status_code == 200
        jsonData = self.response.json()
        assert jsonData['lastName'] == 'Akopyan'

    def test_get_book_by_id(self):
        self.response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/1')
        assert self.response.status_code == 200
        jsonData = self.response.json()
        assert jsonData[0]['idBook'] == 1

