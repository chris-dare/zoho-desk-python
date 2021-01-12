from fastapi import APIRouter

from app.api.v1.endpoints import tickets

api_router = APIRouter()
api_router.include_router(tickets.router, prefix="/tickets", tags=["tickets"])