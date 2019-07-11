.PHONY: build

tag := test-cases:local

build:
	docker build -t $(tag) .

shell:
	docker run -v $(shell pwd):/app -it $(tag) bash
