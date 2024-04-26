# hackathon-toolkit

First, install [Docker](https://docs.docker.com/get-docker/).

Then, to start up the instance, type in the terminal:
```
docker-compose build db && docker-compose up -d db --remove-orphans
make start
```

To shut it down:
```
docker-compose down
```

Links:
[Frontend](http://localhost:3000)
[Postgres Admin](http://localhost:8888)
[Backend](http://localhost:8000)
[Database](http://localhost:5432)