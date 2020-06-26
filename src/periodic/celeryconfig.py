from os import getenv

from dynaconf import settings

_broker_url = settings.CELERY_BROKER_URL
if settings.ENV_FOR_DYNACONF == "heroku":
    _broker_url = getenv("REDIS_URL")

broker_url = _broker_url
imports = ["periodic.tasks"]
result_backend = _broker_url
result_persistent = False
