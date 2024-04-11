SHELL=/bin/bash

TAG=$(shell git rev-parse --short HEAD)
base:
	docker build -t calendar:base -f Dockerfile_base .

image:
	git status
	
	docker build -t lostsquirrel/calendar:$(TAG) -f Dockerfile_b .

push:
	docker push lostsquirrel/calendar:$(TAG)