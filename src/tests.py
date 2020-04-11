test:
	pipenv run python src/manage.py test -v3 project


init:
	pip install pipenv --upgrade
	pipenv install --dev