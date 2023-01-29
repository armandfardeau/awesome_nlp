PWD := $(shell pwd)
PORT ?= 8080
TAG ?= awesome_nlp
WORKERS ?= 4
TIMEOUT ?= 600
LOG_LEVEL ?= INFO

setup:
	python setup_cache.py

start:
	@make setup
	@make build
	@make run

run:
	docker run -it -v $(PWD)/cache:/app/cache -e LOGLEVEL=$(LOGLEVEL) -e TIMEOUT=$(TIMEOUT) -e WORKERS=$(WORKERS) -e DEEPL_API_KEY="$(DEEPL_API_KEY)" -e PORT=$(PORT) -p $(PORT):$(PORT) --rm $(TAG)

build:
	docker build . --compress --tag $(TAG)

bash:
	docker run -it -v $(PWD)/cache:/app/cache -e DEEPL_API_KEY="$(DEEPL_API_KEY)" --rm $(TAG) /bin/bash