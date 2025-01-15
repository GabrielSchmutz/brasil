from fastapi import APIRouter 
from app.services.brasil import *

router = APIRouter()

@router.get("/feriados/{ano}")
async def checkFeriados(ano: int):
    feriados = await getFeriados(ano)
    return feriados 
