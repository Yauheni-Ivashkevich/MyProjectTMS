import multiprocessing
from os import getenv
from pathlib import Path

from dynaconf import settings

_here = Path(__file__).parent.resolve()
assert _here.is_dir(), f"invalid here dir: `{_here!r}`"

_reload = True
_workers = multiprocessing.cpu_count() * 2 + 1  # XXX hahaha classic

_port = getenv("PORT")
assert _port and _port.isdecimal(), f"invalid port: `{_port!r}`"
_port = int(_port)

if settings.ENV_FOR_DYNACONF == "heroku":
    _reload = False

    _workers = getenv("WEB_CONCURRENCY", "4")
    assert _workers and _workers.isdecimal(), f"invalid workers nr: `{_port!r}`"
    _workers = int(_workers)

_src_dir = (_here / "src").resolve()

bind = f"0.0.0.0:{_port}"
chdir = _src_dir.as_posix()
graceful_timeout = 10
max_requests = 200
max_requests_jitter = 20
pythonpath = _src_dir.as_posix()
reload = _reload
timeout = 30
worker_class = "uvicorn.workers.UvicornWorker"
workers = _workers
