PORT := 8080
TAG := awesome_nlp

start:
	@make build
	@make run

run:
	docker run -it -e DEEPL_API_KEY="$(DEEPL_API_KEY)" -e PORT=$(PORT) -p $(PORT):$(PORT) --rm $(TAG)

build:
	docker build . --compress --tag $(TAG)

bash:
	docker run -it -e DEEPL_API_KEY="$(DEEPL_API_KEY)" --rm $(TAG) /bin/bash