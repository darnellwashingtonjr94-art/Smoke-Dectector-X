.PHONY: build run test push clean

IMAGE_NAME = smoke-detector-x

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker-compose up -d

stop:
	docker-compose down

test:
	python -m unittest discover -s tests

logs:
	docker-compose logs -f smoke-detector-x

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf runs/
