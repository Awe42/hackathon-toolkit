.PHONY: start stop

start:
	docker-compose build
	docker-compose up -d

stop:
	docker-compose down

prod:
	docker-compose up -d

explain:
	docker-compose build db && docker-compose up -d db
	cd frontend && (npm run start&)
	cd ../backend/api
	python3 main.py
