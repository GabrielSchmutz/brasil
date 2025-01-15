from fastapi import APIRouter 
from app.services.brasil import *

router = APIRouter()

@router.get("/cep/{cep}")
async def checkCep(cep: int):
    cep = await getCep(cep)
    return cep
