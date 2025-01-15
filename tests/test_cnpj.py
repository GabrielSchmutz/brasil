import pytest
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

def testGetCnpj():
    cnpj = 58325871000165
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    response = requests.get(url)
    assert response.status_code == 200
    if response.status_code == 400:
        print("Erro, você digitou algo de errado")
    data = response.json()
    print(data)

if __name__ == "__main__":
    testGetCep()
