from fastapi import APIRouter

from dbs_assignment.config import settings

router = APIRouter()


@router.get("/v1/hello")
async def hello():
    return {
        'hello': settings.NAME
    }
