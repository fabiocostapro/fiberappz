.PHONY: freeze run

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt
run:
	python run.py