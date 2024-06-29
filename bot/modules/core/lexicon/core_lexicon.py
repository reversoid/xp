from typing import TypedDict


class Lexicon(TypedDict):
    cannot_undertand: str
    cmd_start: str
    cmd_help: str
    fill_username: str
    welcome: str
    username_already_taken: str
    bad_username_message: str
    wrong_username_format: str


CORE_LEXICON: Lexicon = {
    'cmd_start': 'Это твоя площадка для тренировки мышления. Здесь ты будешь развивать свой уникальный метод общения с миром через решение нестандартных задач \n\nДобро пожаловать в твой XP',

    'cmd_help': '/start - начало диалога\n/log_observation — залогировать наблюдение\n/run_experiment — провести свой эксперимент\n/profile — увидеть архив своих наблюдений и экспериментов',

    'cannot_undertand': "Непонятная команда :(",

    'fill_username': 'Введи свой юзернейм',

    'welcome': 'Хей',

    'username_already_taken': 'Это имя уже занято \n\n Попробуй другое',

    'bad_username_message': 'Введи свой юзернейм',

    'wrong_username_format': 'Неподходящий формат для юзернейма. Попробуй заново'
}
