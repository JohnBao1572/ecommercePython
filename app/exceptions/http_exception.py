# Lỗi httpException

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "status_code": exc.status_code
        },
    )

async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code = 500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "detail": str(exc)
        },
    )