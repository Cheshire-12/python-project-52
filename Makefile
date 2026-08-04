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

translate:
	uv run python manage.py makemessages -l ru

makemigrations:
	uv run python manage.py makemigrations

test:
	uv run python manage.py test

shell:
	uv run python manage.py shell