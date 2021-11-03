from fastapi import APIRouter
from config import settings

router = APIRouter(prefix="/persons")

@router.get("/")
async def index() -> dict:
    return {"hello": settings}
