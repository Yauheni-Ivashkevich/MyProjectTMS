from os import getenv
from pathlib import Path

import dj_database_url
from dynaconf import settings as _settings

from project.utils.consts import AGE_1DAY
from project.utils.consts import AGE_1MINUTE

PROJECT_DIR = Path(__file__).parent.resolve()  # /project
BASE_DIR = PROJECT_DIR.parent.resolve()  # /src
REPO_DIR = BASE_DIR.parent.resolve()  # /MyProjectTMS

SECRET_KEY = _settings.SECRET_KEY

DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS

INTERNAL_IPS = [
    "127.0.0.1",
]

# отвечает за активные приложения для данного проекта
INSTALLED_APPS = [
    "django.contrib.admin",  # отвечает за админку
    "django.contrib.auth",  # отвечает за управление пользователями
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # --- my apps ---
    "apps.index",
    "apps.resume",
    "apps.projects",
    "apps.users",
    #"apps.blog.appsBlogConfig", (для пакета blog)
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [PROJECT_DIR / "jinja2", ],  # где искать шаблоны
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "project.utils.jinja2env.build_jinja2_environment",
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

_db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    _db_url = getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(_db_url, conn_max_age=600),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"  # XXX: DO NOT EVER THINK ABOUT TOUCHING THIS
LOCAL_TIME_ZONE = _settings.LOCAL_TIME_ZONE

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/assets/"  # путь от которого все отсчитывается на разных сервисах

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

STATIC_ROOT = REPO_DIR / ".static"  # куда соберется вся статика после команды collectstatic - папка создается.
# в джанге куча статики в разных местах и разных приложениях

# LOGIN_URL = reverse_lazy("onboarding:sign_in")
# LOGIN_REDIRECT_URL = reverse_lazy("blog:post:all_post")

