from datetime import datetime

from fastapi import APIRouter

from dbs_assignment.config import settings

router = APIRouter()


@router.get("/v1/status")
async def status():
    return {
        "timestamp": datetime.now().isoformat(),
        'hello': settings.NAME
    }
