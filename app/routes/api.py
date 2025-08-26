from fastapi import APIRouter

from app.controllers import auth_controller, category_controller, role_controller, user_controller


api_router = APIRouter()
api_router.include_router(user_controller.router)
api_router.include_router(role_controller.router)
api_router.include_router(auth_controller.router)
api_router.include_router(category_controller.router)