from fastapi import APIRouter 
from app.services.brasilapi import *

router = APIRouter()

@router.get("/cnpj/{cnpj}")
async def checkCnpj(cnpj: int):
    cnpj = await getCnpj(cnpj)
    return cnpj
