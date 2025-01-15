from fastapi import FastAPI
from app.api import cep, ddd, cnpj, feriados

app = FastAPI()

app.include_router(cep.router)
app.include_router(ddd.router)
app.include_router(cnpj.router)
app.include_router(feriados.router)
