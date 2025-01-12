""" This module contains the settings for the chatGMT user app """
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ This class contains the settings for the chatGMT user app """
    # Names etc.
    FOOTER_TEXT: str = "© 2024"
    # Paths
    ASSET_FOLDER: str = "frontend/assets"
    PAGES_FOLDER: str = "frontend/pages"
    # LOGO_FILE: str = ".png"

    # Technical Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DEBUG_MODE: bool = False

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
