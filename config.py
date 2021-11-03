from pydantic import BaseSettings
from functools import lru_cache

class GlobalConfig(BaseSettings):
    API_V1: str = "/api/v1"
    DATABASE_URL: str

    class Config:
        env_file: str = ".env"

@lru_cache()
def get_configuration() -> GlobalConfig:
    return GlobalConfig()

settings = get_configuration()    
