SHELL=/bin/bash

TAG=$(shell git rev-parse --short HEAD)
image:
	git status
	
	docker build -t ccr.ccs.tencentyun.com/lu520/calendar:$(TAG) .

tx:
	docker push ccr.ccs.tencentyun.com/lu520/calendar:$(TAG)