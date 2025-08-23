

from fastapi import HTTPException
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.config.database import Base, engine, get_db
from app.exceptions.http_exception import http_exception_handler
from app.swagger.swagger_config import custom_openapi

from sqlalchemy.orm import Session
from sqlalchemy import text 
from app.routes.api import api_router

# # Khởi tạo DB (tạo bảng nếu chưa có)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing database...")
    # Tạo bảng nếu chưa có
    Base.metadata.create_all(bind=engine)
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))   
        print("Database connected successfully")
    except Exception as e:
        print(f"Database connection failed: {e}")    
    yield
    print("Application shutdown")

app = FastAPI(
    title="E-commerce API",
    docs_url="/api/docs",       
    redoc_url="/api/redoc",     
    openapi_url="/api/openapi.json",
    lifespan=lifespan
    )

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, http_exception_handler)
# Swagger
app.openapi = lambda: custom_openapi(app)

# Route test
@app.get("/")
def home():
    return {"message": "E-commerce API is running 🚀"}

app.include_router(api_router, prefix="/api")
