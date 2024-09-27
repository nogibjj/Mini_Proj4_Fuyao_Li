install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

test: 
	python -m pytest -cov=main test_main.py

lint:
	ruff check *.py mylib/*.py test_*.py *.ipynb

deploy:

generate_and_push:
	python test_main.py

	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Generate result.md"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi


all: install format lint test deploy