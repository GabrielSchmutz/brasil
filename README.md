# Brasil

Este projeto é uma aplicação Python que utiliza a [BrasilAPI](https://brasilapi.com.br) para oferecer serviços de consulta de informações como **CEP**, **DDD**, **CNPJ**, e **Feriados**. A aplicação é construída usando o **FastAPI** para criar um painel interativo, permitindo que o usuário faça consultas através de uma interface web.

---

**Instalação e dependências**
1- Clone o repositório
```
git clone https://codeberg.org/gps/brasil
cd brasil
```

2- Crie um ambiente virtual usando o [Pyenv](https://github.com/pyenv/pyenv)
```
```
pyenv virtualenv 3.12.5 brasil
pyenv global brazil
```
```

3- Instale as dependências e rode o projeto

```
```
pip install requirements.txt -r
uvicorn app.main:app --reload
```
```
