# Brasil 🇧🇷

Este projeto é uma aplicação Python que utiliza a [BrasilAPI](https://brasilapi.com.br) para oferecer serviços de consulta de informações como **CEP**, **DDD**, **CNPJ**, e **Feriados**.

## Instalação e dependências

1 - Clone o repositório
```
git clone https://codeberg.org/gps/brasil
cd brasil
```

2 - Crie um ambiente virtual usando o [Pyenv](https://github.com/pyenv/pyenv)
```
pyenv virtualenv 3.12.5 brasil
pyenv global brazil
```

3 - Instale as dependências e rode o projeto

```
pip install requirements.txt -r
uvicorn app.main:app --reload
```
4 - Acesse o painel
Abra seu navegador e vá até o endereço ``http://127.0.0.1:8000/docs``


## Docker 🐳

1 - Certifique-se que o Docker está instalado na sua máquina. Se ao digitar ``docker version`` aparecer ``bash: command not found: docker`` siga o guia no site [DockerDocs](https://docs.docker.com/engine/install/)

2 - Contrua a imagem
```
docker build .
```

3 - Inicialize o container
```
docker run -it -e PORT=8000
```
