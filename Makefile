COMPOSE = docker compose -p robot -f docker/compose/base.yml -f docker/compose/web.yml -f docker/compose/ros.yml

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f --tail=200

rebuild:
	$(COMPOSE) build --no-cache

ps:
	$(COMPOSE) ps

restart:
	$(COMPOSE) down && $(COMPOSE) up -d
