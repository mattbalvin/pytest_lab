# setup:
# create the venv
#	python3 -m venv ~/.pytest_lab

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=pytest_lab_cov test/*.py
	python -m pytest --nbval notebook.ipynb
	
lint:
	pyline --disable=R,C myrepolib cli web

all: install test lint
