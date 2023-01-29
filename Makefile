PWD := $(shell pwd)
PORT := 8080
TAG := awesome_nlp
WORKERS := 4
TIMEOUT := 600
PRELOAD_PIPELINES := "true"

download:
	ls -d cache/* | xargs -I {} bash -c "cd '{}' && git lfs pull"

start:
	@make download
	@make build
	@make run

run:
	docker run -it -v $(PWD)/cache:/app/cache -e PRELOAD_PIPELINES=$(PRELOAD_PIPELINES) -e TIMEOUT=$(TIMEOUT) -e WORKERS=$(WORKERS) -e DEEPL_API_KEY="$(DEEPL_API_KEY)" -e PORT=$(PORT) -p $(PORT):$(PORT) --rm $(TAG)

build:
	docker build . --compress --tag $(TAG)

bash:
	docker run -it -v $(PWD)/cache:/app/cache -e DEEPL_API_KEY="$(DEEPL_API_KEY)" --rm $(TAG) /bin/bash