

build:
	docker build -t loadswatch .

run:
	docker run -v /var/run/docker.sock:/var/run/docker.sock -it --rm loadswatch
