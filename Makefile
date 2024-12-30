# Variáveis
DOCKER_COMPOSE = docker-compose
SERVICE_NAME = flask-app
HOST_DB = db

# Comandos
build:
	$(DOCKER_COMPOSE) up --build

up:
	$(DOCKER_COMPOSE) up

down:
	$(DOCKER_COMPOSE) down --volumes

restart:
	$(DOCKER_COMPOSE) down --volumes && $(DOCKER_COMPOSE) up --build

logs:
	$(DOCKER_COMPOSE) logs -f $(SERVICE_NAME)

exec:
	$(DOCKER_COMPOSE) exec $(SERVICE_NAME) bash

create_tables:
	$(DOCKER_COMPOSE) exec $(SERVICE_NAME) python manage.py

db:
	$(DOCKER_COMPOSE) exec $(HOST_DB) mysql -u guido -p

prune:
	docker system prune -f

req:
	pip freeze > app/requirements.txt