from fastapi import APIRouter
from app.services.brasilapi import *

router = APIRouter()

@router.get("/ddd/{ddd}")
async def checkDdd(ddd: int):
    ddd = await getDdd(ddd)
    return ddd
