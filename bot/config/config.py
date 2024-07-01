from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Api:
    url: str
    api_key: str


@dataclass
class Redis:
    host: str
    port: int
    password: str


@dataclass
class Database:
    redis: Redis


@dataclass
class Config:
    bot: TgBot
    api: Api
    database: Database


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    bot = TgBot(token=env('BOT_TOKEN'))
    api = Api(url=env('API_URL'), api_key=env('API_KEY'))
    redis = Redis(host=env('REDIS_HOST'), password=env(
        'REDIS_PASSWORD'), port=int(env('REDIS_PORT')))
    database = Database(redis=redis)

    return Config(bot=bot, api=api, database=database)
