from fastapi import APIRouter
from app.services.swagger_service import SwaggerService

router = APIRouter()

@router.get("/")
def list_endpoints():
    return SwaggerService.list_endpoints()
