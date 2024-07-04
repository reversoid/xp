from typing import TypedDict


class Lexicon(TypedDict):
    log_observation: str
    log_observation_success: str
    no_data: str


LEXICON: Lexicon = {
    "log_observation": """
        Наблюдение может принимать любую форму: слово, скриншот, манифест, голосовое или видео. \n\nЧто пробудило любопытство в тебе сегодня?
    """,
    "log_observation_success": "Наблюдение залогировано",
    "no_data": """
        Нет данных для наблюдения. Одно наблюдение – одно сообщение
    """,
}
