help:
	@echo "dev  		install development packages"
	@echo "setup 		install pingo"
	@echo "test 		run default test suit"
	@echo "test-cov  	run default test suit with coverage"
	@echo "test-pep  	run default test suit with pep8"


dev:
	pip install -r requirements.txt


setup:
	python setup.py install


test:
	py.test pingo


test-cov:
	py.test pingo --cov pingo --cov-report html


test-pep:
	py.test pingo --pep8
