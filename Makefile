install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

test: 
	python -m pytest -cov=main test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

all: install format lint test