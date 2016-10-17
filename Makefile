

build:
	docker build -t loadswatch .

run:
	docker run -v /var/run/docker.sock:/var/run/docker.sock -it --rm -e AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) -e AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY) loadswatch
