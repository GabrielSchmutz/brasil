from fastapi import FastAPI
from app.endpoint import cep, ddd, cnpj, feriados, domain

app = FastAPI()

app.include_router(cep.router)
app.include_router(ddd.router)
app.include_router(cnpj.router)
app.include_router(feriados.router)
app.include_router(domain.router)
