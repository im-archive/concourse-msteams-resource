user=aricwhitaker3
name=msteams-resource
docker=docker
tag=$(user)/$(name)
dockerfile=Dockerfile

push: build
	$(docker) push $(tag)

build:
	$(docker) build -t $(tag) -f $(dockerfile) .

