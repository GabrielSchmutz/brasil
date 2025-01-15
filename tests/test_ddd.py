import pytest
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

def testGetDdd():
    ddd = 21
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    response = requests.get(url)
    assert response.status_code == 200
    if response.status_code == 400:
        print("Erro, você digitou algo de errado")
    data = response.json()
    print(data)

if __name__ == "__main__":
    testGetCep()
