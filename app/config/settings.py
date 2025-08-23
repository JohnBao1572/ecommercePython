from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    DB_HOST: str 
    DB_PORT: int 
    DB_USER: str 
    DB_PASS: str 
    DB_NAME: str 
    JWT_SECRET: str 
    JWT_ALGORITHM: str 

    class Config:
        env_file = ".env"  
        env_file_encoding = "utf-8"

settings = Setting()
