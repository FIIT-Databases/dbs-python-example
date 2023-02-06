from fastapi import APIRouter

from dbs_assignment.endpoints import hello

router = APIRouter()
router.include_router(hello.router, tags=["hello"])
