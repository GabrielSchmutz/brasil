import httpx

async def getCep(cep: int):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 500:
        return {"Erro": "Erro interno do servidor, tente novamente mais tarde."}
    else:
        return {"Erro": f"{cep} Não é um CEP válido."}


async def getDdd(ddd: int):
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 500:
        return {"Erro": "Erro interno do servidor, tente novamente mais tarde."}
    else:
        return {"Error": f"{ddd} não é um DDD válido."}


async def getCnpj(cnpj: int):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 500:
        return {"Erro": "Erro interno do servidor, tente novamente mais tarde."}
    else:
        return {"Erro": f"{cnpj} não é um CNPJ válido."}


async def getFeriados(ano: int):
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 500:
        return {"Erro": "Erro interno do servidor, tente novamente mais tarde."}
    else:
        return {"Erro": f"Erro. Coloque um ano (e.g: 2025)"}


async def getDomain(domain: str):
    url = f"https://brasilapi.com.br/api/registrobr/v1/{domain}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 500:
        return {"Erro": "Erro interno do servidor, tente novamente mais tarde."}
    else:
        return {"Erro": f"Erro. Digite um domínio válido."}
