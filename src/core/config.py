from pydantic_settings import BaseSettings, SettingsConfigDict  


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8',)

    DB_USER:str
    DB_PASSWORD:str
    DB_HOST:str
    DB_PORT:str
    DB_NAME:str

    db_echo:bool = False

    api_v1_prefix:str = "/api/v1"

    def get_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings(_env_file='db.env', _env_file_encoding='utf-8', db_echo=True)
print(settings.get_url())