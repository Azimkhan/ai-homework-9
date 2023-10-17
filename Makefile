# Commands
LOCAL_TAG := dino-dragon:test
REMOTE_TAG := 911571086818.dkr.ecr.us-east-1.amazonaws.com/dino-dragon:latest
REPO_URL := 911571086818.dkr.ecr.us-east-1.amazonaws.com

build:
	docker build -t $(LOCAL_TAG) .

tag:
	docker tag  $(LOCAL_TAG) $(REMOTE_TAG)

push:
	docker push $(REMOTE_TAG)

login:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $(REPO_URL)

all: build tag push