from fastapi import APIRouter
from app.services.brasil import *

router = APIRouter()

@router.get("/domain/{domain}")
async def checkDomain(domain: str):
    domain = await getDomain(domain)
    return domain
