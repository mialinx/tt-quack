up:
	docker-compose up --detach

test: up
	docker-compose exec webapp python3 /app/manage.py test

migrate: up
	docker-compose exec webapp python3 /app/manage.py migrate

lint: up
	docker-compose exec webapp pylint /app
