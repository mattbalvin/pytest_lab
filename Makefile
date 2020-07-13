# setup:
# create the venv
#	python3 -m venv ~/.pytest_lab

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=libpoc tests/*.py
	python -m pytest --nbval poc_notebook.ipynb
	
#format:
#	black *.py

#lint: format
lint:
	python -m pylint --disable=R,C pocapp

all: install test lint
