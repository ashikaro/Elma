build:
	docker build --tag elma-app .

run: rm
	docker run --name elma -v $(PWD):/usr/src -it elma-app /bin/sh

rm:
	docker rm -f elma

test:
	python -m unittest

docs:
	doxygen elmadocs.config

