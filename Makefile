dev:
	docker-compose up

migrate:
	./scripts/migrate.sh

deploy:
	./scripts/deploy.sh

test:
	pytest --cov=backend tests/