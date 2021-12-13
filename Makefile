
MAIN_DIR=src/main
TESTS_DIR=src/test

build:
	python setup.py sdist

test:
	cd $(MAIN_DIR)\
	python -m pytest $(TESTS_DIR)

publish:
	twine upload --repository pypi dist/*

clean:
	rm -r dist/ build/
