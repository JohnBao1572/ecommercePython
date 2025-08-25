from fastapi import APIRouter

from app.controllers import role_controller, user_controller


api_router = APIRouter()
api_router.include_router(user_controller.router)
api_router.include_router(role_controller.router)