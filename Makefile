PORT := 8080
TAG := awesome_nlp

start:
	@make build
	@make run

run:
	docker run -it -e PORT=$(PORT) -p $(PORT):$(PORT) --rm $(TAG)

build:
	docker build . --compress --tag $(TAG)

bash:
	docker run -it --rm $(TAG) /bin/bash