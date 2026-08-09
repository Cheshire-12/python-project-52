#!/usr/bin/env bash
# скачиваем uv
curl --proto "=https" -LsSf https://astral.sh | sh
source $HOME/.local/bin/env

# здесь добавьте все необходимые команды для установки вашего проекта
# команду установки зависимостей, сборки статики, применения миграций и другие
make install && make collectstatic && make migrate && make compilemessages