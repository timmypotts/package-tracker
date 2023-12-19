.PHONY: up
up:
	docker-compose up -d --build
	docker-compose logs -f

.PHONY: down
down:
	docker-compose down -v

.PHONY: restart
restart:
	docker-compose restart
	docker-compose logs -f api

.PHONY: restart_hard
restart_hard:
	docker-compose down -v
	docker-compose up -d --build
	docker-compose logs -f