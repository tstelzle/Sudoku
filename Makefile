# MAKEFILE https://github.com/tstelzle/Sudoku
# AUTHORS: Tarek Stelzle

IMAGE-NAME := python-env-sudoku
CONTAINER-NAME := sudoku
MOUNT-DIR := $(PWD)
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
RUN := docker exec -it -w /usr/src $(CONTAINER-NAME) python main.py
IGNORE-OUTPUT := > /dev/null 2>&1

.PHONY: default build-image container run run-master

default:
	 @echo "Possible Commands:"
	 @echo " build-image     - Builds the image."
	 @echo " container       - Runs the container."
	 @echo " run             - Runs the main file of the 'Sudoku' repository."

build-image:
	docker build -t $(IMAGE-NAME) .

container:
	docker run -d -t --rm -v $(MOUNT-DIR):/usr/src --name $(CONTAINER-NAME) $(IMAGE-NAME)

run:
	$(RUN)

run-master:
	git stash --include-untracked $(IGNORE-OUTPUT)
	git checkout master $(IGNORE-OUTPUT)
	$(RUN)
	git checkout $(BRANCH) $(IGNORE-OUTPUT)
	git stash pop $(IGNORE-OUTPUT)