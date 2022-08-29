IMAGE=desci-viewer
CONTAINER=desci-viewer
PORT=5000

image:
	docker build -t $(IMAGE) .

run-win: image
	docker run -it --name $(CONTAINER) --volume $(shell cmd /c cd)/commits:/app/commits -p $(PORT):5000 $(IMAGE)

run-linux: image
	docker run -it --name $(CONTAINER) --volume $(shell pwd)/commits:/app/commits -p $(PORT):5000 $(IMAGE)

rm:
	docker rm -f $(CONTAINER)
