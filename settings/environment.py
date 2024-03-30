from functools import lru_cache

from pydantic.v1 import BaseSettings


class Environment(BaseSettings):
    BOT_KEY: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str


@lru_cache
def get_environment() -> Environment:
    return Environment()
