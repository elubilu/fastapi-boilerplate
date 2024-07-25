import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Boilerplate"
    admin_email: str = "admin@example.com"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
