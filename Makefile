HERE := $(shell pwd)
VENV := $(shell pipenv --venv)
PYTHONPATH := ${HERE}/src
TEST_PARAMS := --verbosity 2 --pythonpath ${PYTHONPATH}
PSQL_PARAMS := --host=localhost --username=alex --password


ifeq ($(origin PIPENV_ACTIVE), undefined)
	RUN := pipenv run
endif

ifeq ($(ENV_FOR_DYNACONF), travis)
	RUN :=
	TEST_PARAMS := --failfast --keepdb --verbosity 0 --pythonpath ${PYTHONPATH}
	PSQL_PARAMS := --host=localhost --username=postgres --no-password
else ifeq ($(ENV_FOR_DYNACONF), heroku)
	RUN :=
endif


MANAGE := ${RUN} python src/manage.py


.PHONY: format
format:
	${RUN} isort --virtual-env ${VENV} --recursive --apply ${HERE}
	${RUN} black ${HERE}


.PHONY: run
run: static
	${MANAGE} runserver


.PHONY: beat
beat:
	PYTHONPATH=${PYTHONPATH} \
	${RUN} celery worker \
		--app periodic.app -B \
		--config periodic.celeryconfig \
		--workdir ${HERE}/src \
		--loglevel=info


.PHONY: docker
docker: wipe
	docker-compose build


.PHONY: docker-run
docker-run: docker
	docker-compose up


.PHONY: static
static:
	${MANAGE} collectstatic --noinput --clear -v0


.PHONY: migrations
migrations:
	${MANAGE} makemigrations


.PHONY: migrate
migrate:
	${MANAGE} migrate


.PHONY: su
su:
	${MANAGE} createsuperuser


.PHONY: sh
sh:
	${MANAGE} shell


.PHONY: test
test:
	set ENV_FOR_DYNACONF=test
	${RUN} coverage run \
		src/manage.py test ${TEST_PARAMS} \
			apps \
			periodic \
			project \

	${RUN} coverage report
	${RUN} isort --virtual-env ${VENV} --recursive --check-only ${HERE}
	${RUN} black --check ${HERE}


.PHONY: report
report:
	${RUN} coverage html --directory=${HERE}/htmlcov --fail-under=0
	open "${HERE}/htmlcov/index.html"


.PHONY: venv
venv:
	pipenv install --dev


.PHONY: clean
clean:
	${RUN} coverage erase
	rm -rf htmlcov
	find . -type d -name "__pycache__" | xargs rm -rf
	rm -rf ./.static/


.PHONY: clean-docker
clean-docker:
	docker-compose stop || true
	docker-compose down || true
	docker-compose rm --force || true
	docker system prune --force


.PHONY: wipe
wipe: clean clean-docker


.PHONY: resetdb
resetdb:
	psql ${PSQL_PARAMS} \
		--dbname=postgres \
		--echo-all \
		--file=${HERE}/ddl/reset_db.sql \
		--no-psqlrc \
		--no-readline \


.PHONY: initdb
initdb: resetdb migrate