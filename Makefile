PIPENV ?= PYTHONPATH=src pipenv run

get-certificates:
	bash get_certificates.sh

preprocess-data:
		$(PIPENV) python src/preprocess/preprocess.py

dashboard:
		$(PIPENV) python src/app/index.py

clean-certificates:
	rm -f data/certificates/*
.PHONY: clean-certificates

clean-pickle-files:
	rm -f data/*.pickle
.PHONY: clean-pickle-files

clean-all: clean-certificates clean-pickle-files
.PHONY: clean-all

all: clean-all get-certificates preprocess-data dashboard
.PHONY: all

make heroku-local:
	heroku local web

