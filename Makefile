install:
	uv sync

build:
	./build.sh

collectstatic:
	uv run python manage.py collectstatic --no-input

migrate:
	uv run python manage.py migrate
	
compilemessages:
	uv run python manage.py compilemessages

render-start:
	uv run gunicorn task_manager.wsgi

dev:
	uv run python manage.py runserver