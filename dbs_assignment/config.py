from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    class Config:
        case_sensitive = True

    NAME: str

settings = Settings()
