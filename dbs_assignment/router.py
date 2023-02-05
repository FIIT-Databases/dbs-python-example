from fastapi import APIRouter

from dbs_assignment.endpoints import status

router = APIRouter()
router.include_router(status.router, tags=["status"])
