HERE := $(shell pwd)
BRANCH := $(shell git branch --quiet --no-color | grep '*' | sed -e 's/^\*\ //g')
UNTRACKED := $(shell git status --short | grep -e '^[ ?]' | wc -l | sed -e 's/\ *//g')
UNTRACKED2 := $(shell git status --short | awk '{print substr($$0, 2, 2)}' | grep -e '\w\+' | wc -l | sed -e 's/\ *//g')


run: static
	DJANGO_DEBUG=TRUE pipenv run python src/manage.py runserver


runa: static
	PYTHONPATH="${HERE}/src" pipenv run uvicorn project.asgi:application


static:
	DJANGO_DEBUG=TRUE pipenv run python src/manage.py collectstatic --noinput --clear -v0


test:
	DJANGO_DEBUG=TRUE pipenv run python src/manage.py test -v2 project apps


deploy: clean
	@echo 'test branch...'
	test "${BRANCH}" = "master"
	@echo 'test untracked...'
	test "${UNTRACKED}" = "0"
	@echo 'test untracked 2...'
	test "${UNTRACKED2}" = "0"
	git commit --message "MAKE DEPLOY @ $(shell date)" --edit
	git push origin master


install: clean
	pipenv update --dev


clean:
	find . -type d -name "__pycache__" | xargs rm -rf
	rm -rf Pipfile.lock
	rm -rf ./.static/

.PHONY: run runa static test deploy install clean