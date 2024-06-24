# XP bot

This a telegram bot for XP

## How to run bot in dev mode
1. You must have [docker](https://www.docker.com/products/docker-desktop/) running
2. You must have [Poetry](https://python-poetry.org/docs/#installation) installed
3. Create `.env` file. You can use `.env.example` as an example. For dev purposes u can just copy it without any editing: docker-compose and python-env will use the same .env file.
4. Run `poetry shell`
5. Run `poetry install` to install dependencies.
6. Run `./dev.sh` to run bot
