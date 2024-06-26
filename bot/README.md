# XP bot

This a telegram bot for XP

## How to run bot in dev mode
1. You must have [docker](https://www.docker.com/products/docker-desktop/) running
2. You must have [Poetry](https://python-poetry.org/docs/#installation) installed
3. Create `.env` file. You can use `.env.example` as an example. For dev purposes u can just copy it without any editing: docker-compose and python-env will use the same .env file.
4. Run `poetry shell`
5. Run `poetry install` to install dependencies.
6. Run `./dev.sh` to run bot


## Зависимости
[aiogram](https://docs.aiogram.dev/en/latest/) – все для интеграции с API телеграм ботов.
[pydantic](https://docs.pydantic.dev/latest/) – все для валидации данных. 

## Архитектура
Приложение состоит из модулей и shared-директории.

В shared-директории лежат глобальный lexicon, сущности, использующиеся в боте, утилиты и api-service, от которого наследуются все сервисы, которые делают http-запросы к бекенду.

Каждый модуль имеет свой смысл и состоит из следующих слоев:

### Handlers
Описывают, как боту реагировать на то или иное действие.

### Keyboards
Клавиатуры, кнопки, которые отправляются пользователю. Используются слоем **handlers**.

### Lexicon
Содержит словари `semantic_code` -> `translated text`. Используются слоем **handlers**.


`semantic_code` не отображается пользователю, но используется разработчиком. Название должно быть коротким и понятным. 
`translated_text` отображается пользователю.


### States
Хранимые состояния пользователя, например `filling_experiment` или `scrolling_feed`.

### Middlewares
Reference to [aiogram docs](https://docs.aiogram.dev/en/dev-3.x/dispatcher/middlewares.html)

### Services
Логический слой. Делает transform входных / выходных данных. Делает запросы к бекенду, кидает семантические ошибки, которые должны быть перехвачены.
