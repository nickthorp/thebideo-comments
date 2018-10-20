init:
	python3 -m virtualenv env
	source env/bin/activate
	which python3
	pip install -r requirements.txt

build:
	python3 package.py
