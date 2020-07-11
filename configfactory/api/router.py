from fastapi import APIRouter

router = APIRouter()


@router.get("/environments")
async def get_environment():
    return []
