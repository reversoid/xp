from typing import TypedDict


class Lexicon(TypedDict):
    log_observation: str
    log_observation_success: str
    not_supported_data: str


LEXICON: Lexicon = {
    "log_observation": """
        Наблюдение может принимать любую форму: слово, скриншот, манифест, голосовое или видео. \n\nЧто пробудило любопытство в тебе сегодня?
    """,
    "log_observation_success": "Наблюдение залогировано",
    "not_supported_data": """
        Такой формат не поддерживается. Попробуйте загрузить что-то другое
    """,
}
