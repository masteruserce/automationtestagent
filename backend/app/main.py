from fastapi import FastAPI
from backend.app.routers import swagger as swagger_router
from backend.app.routers import intent as intent_router
from backend.app.routers import scenarios as scenario_router
from backend.app.routers import generation as generation_router
from backend.app.routers import bdd as bdd_router

app = FastAPI(title="Automation Agent Backend")

app.include_router(swagger_router.router)
app.include_router(intent_router.router)
app.include_router(scenario_router.router)
app.include_router(generation_router.router)
app.include_router(bdd_router.router)
