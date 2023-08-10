from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Api:
    url: str
    api_secret: str


@dataclass
class Config:
    bot: TgBot
    api: Api


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path, recurse=False)
    return Config(bot=TgBot(token=env('BOT_TOKEN')), api=Api(url=env('API_URL'), api_secret=env('API_SECRET')))
