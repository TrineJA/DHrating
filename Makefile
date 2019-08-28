PIPENV ?= PYTHONPATH=src pipenv run

get-certificates:
	bash get_certificates.sh

preprocess-data:
		$(PIPENV) python src/preprocess/preprocess.py

dash-local:
		$(PIPENV) python src/app/index.py

heroku-local:
	heroku local web

clean-certificates:
	rm -f data/certificates/*
.PHONY: clean-certificates

clean-pickle-files:
	rm -f data/*.pickle
.PHONY: clean-pickle-files

clean-all: clean-certificates clean-pickle-files
.PHONY: clean-all

all: clean-all get-certificates preprocess-data dash-local
.PHONY: all