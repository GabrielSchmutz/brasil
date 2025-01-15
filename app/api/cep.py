from fastapi import APIRouter 
from app.services.brasilapi import *

router = APIRouter()

@router.get("/cep/{cep}")
async def checkCep(cep: int):
    cep = await getCep(cep)
    return cep
