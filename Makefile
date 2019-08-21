get-certificates:
	bash get_certificates.sh

preprocess-data:
		$(PIPENV) python src/preprocess/preprocess.py

dashboard:
		$(PIPENV) python src/app/index.py

make clean-certificates:
	rm -f data/certificates/*
.PHONY: clean-certificates

make clean-pickle-files:
	rm -f data/*.pickle
.PHONY: clean-pickle-files

make clean-all: clean-certificates clean-pickle-files
.PHONY: clean-all

all: clean-all get-certificates preprocess-data dashboard
.PHONY: all

