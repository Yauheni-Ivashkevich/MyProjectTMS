FROM python:3.8-alpine

ENV ENV_FOR_DYNACONF docker
ENV PIPENV_CACHE_DIR /app/.pipenv_cache
ENV PIPENV_COLORBLIND 1
ENV PIPENV_HIDE_EMOJIS 1
ENV PIPENV_INSTALL_TIMEOUT 120
ENV PIPENV_MAX_RETRIES 2
ENV PIPENV_NOSPIN 1
ENV PIPENV_TIMEOUT 30
ENV PIPENV_VENV_IN_PROJECT 1
ENV PIPENV_YES 1

RUN apk --no-cache --update --virtual build-dependencies add \
    bash \
    g++ \
    libffi-dev \
    make \
    postgresql-dev \
    python3-dev \
    || exit 1

RUN pip install \
    pipenv \
    || exit 1

WORKDIR /app/

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --deploy

COPY ./ ./

RUN make static

EXPOSE 80

ENTRYPOINT ["./run-gunicorn.sh"]