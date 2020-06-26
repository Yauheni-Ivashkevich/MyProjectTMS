#!/bin/bash

echo "RELEASING WEB"

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. >/dev/null 2>&1 && pwd)"

cd "${PROJECT_DIR}" || exit 1

make migrate

echo "DONE: RELEASING WEB"