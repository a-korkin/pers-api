import os 
from pydantic import BaseSettings

class GlobalConfig(BaseSettings):
    API_V1 = "/api/v1"
