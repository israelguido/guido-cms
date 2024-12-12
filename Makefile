# Variáveis
DOCKER_COMPOSE = docker-compose
SERVICE_NAME = flask_app

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

prune:
	docker system prune -f

req:
	pip freeze > requirements.txt
