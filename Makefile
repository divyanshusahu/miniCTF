docker_build:
	docker build -t minictf .

docker_run:
	docker run --rm -it -p 8000:8000 minictf:latest
