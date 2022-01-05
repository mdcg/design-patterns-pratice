import yaml
from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    type: str
    database: str
    host: str
    port: int
    username: str
    password: str


def get_config():
    data_loaded = {}
    with open("config.yaml", "r") as stream:
        data_loaded = yaml.safe_load(stream)

    return DatabaseConfig(**data_loaded["database"])
