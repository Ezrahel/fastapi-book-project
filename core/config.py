import os
import secrets

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "hng12-stage2"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "HNG12 DEVOPS x BACKEND (Stage 2)"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False
    SLACK_TARGET_URL:str=os.getenv("SLACK_TARGET_URL", "")
    BASE_URL_IP:str=os.getenv("TICK_URL","http://102.37.138.135/")
    TICK_URL:str=f"http://{BASE_URL_IP}/telex-webhook"


settings = Settings()
