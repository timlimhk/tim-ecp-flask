
## Composes test environment using docker-compose
build:
	docker-compose -f ./docker-compose.yml build
stop:
	docker-compose -f ./docker-compose.yml down -v
deploy:
	docker-compose -f ./docker-compose.yml up -d --force-recreate
