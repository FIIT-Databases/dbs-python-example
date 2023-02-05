from fastapi import FastAPI

from dbs_assignment.router import router

app = FastAPI(title="DBS")
app.include_router(router)
