#!/bin/bash

echo "RUNNING WEB"

sleep 60 # I LOVE DOCKER

DOCKER_SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

"${DOCKER_SCRIPTS}/release-web.sh"

PROJECT_DIR="$(cd "${DOCKER_SCRIPTS}/.." >/dev/null 2>&1 && pwd)"

cd "${PROJECT_DIR}" || exit 1

pipenv run "${PROJECT_DIR}/run-gunicorn.sh"

echo "DONE: RUNNING WEB"