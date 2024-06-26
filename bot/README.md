# XP bot

This a telegram bot for XP

## How to run bot in dev mode
1. You must have [docker](https://www.docker.com/products/docker-desktop/) running
2. You must have [Poetry](https://python-poetry.org/docs/#installation) installed
3. Create `.env` file. You can use `.env.example` as an example. For dev purposes u can just copy it without any editing: docker-compose and python-env will use the same .env file.
4. Run `poetry shell`
5. Run `poetry install` to install dependencies.
6. Run `./dev.sh` to run bot


## Architecture
Application consists of modules.

Each module can have the following layers:

### Handlers
Describe how the bot react to button clicks, commands, messages.

### Keyboards
Keyboards, buttons and other stuff to send to user. Always used by **handlers**.

### Lexicon
Contains dictionaries: `semantic_code` -> `translated text`.

Semantic code is not shown anywhere except from code. It should be clear for developer. 
Translated text is shown to user.

For example semantic code "experiment_started" is translated to "You have some hours to do something..."

### States
Current step for user. For example, "scrolling feed" or "viewing profile".

### Middlewares
Reference to [aiogram docs](https://docs.aiogram.dev/en/dev-3.x/dispatcher/middlewares.html)

### Services
Logic layer. Does some stuff about data transformations. Makes http requests to backend, throws application errors.

