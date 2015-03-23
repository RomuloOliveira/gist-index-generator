clean:
	@find -name '*.pyc' -delete

build: clean
	# build

requirements: clean
	@pip install -r requirements.txt

requirements-dev: clean
	@pip install -r requirements-dev.txt

lint: clean
	@flake8 .

test: clean build
	# tests

coverage: tests
	# coverage
