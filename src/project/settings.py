from os import getenv
from pathlib import Path

import dj_database_url
from django.urls import reverse_lazy
from dynaconf import settings as _settings

from project.utils.consts import AGE_1DAY
from project.utils.consts import AGE_1MINUTE

PROJECT_DIR = Path(__file__).parent.resolve()  # /project
BASE_DIR = PROJECT_DIR.parent.resolve()  # /src
REPO_DIR = BASE_DIR.parent.resolve()  # /MyProjectTMS

SECRET_KEY = _settings.SECRET_KEY

DEBUG = _settings.DEBUG
PROFILING = _settings.PROFILING

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS_ORDERED = {
    0: "django.contrib.admin",  # отвечает за админку
    10: "django.contrib.auth",  # отвечает за управление пользователями
    20: "django.contrib.contenttypes",
    30: "django.contrib.sessions",
    40: "django.contrib.messages",
    50: "django.contrib.staticfiles",
    60: "django.contrib.sites",
    # --- my apps ---
    1000: "apps.index",
    2000: "apps.resume",
    3000: "apps.projects",
    4000: "apps.onboarding.apps.OnboardingConfig",
    5000: "apps.feedback",
}
if PROFILING:
    INSTALLED_APPS_ORDERED[49] = "silk"

INSTALLED_APPS = [app for _, app in sorted(INSTALLED_APPS_ORDERED.items())]

MIDDLEWARE_ORDERED = {
    0: "django.middleware.security.SecurityMiddleware",
    10: "django.contrib.sessions.middleware.SessionMiddleware",
    20: "whitenoise.middleware.WhiteNoiseMiddleware",
    30: "django.contrib.sessions.middleware.SessionMiddleware",
    40: "django.middleware.common.CommonMiddleware",
    50: "django.middleware.csrf.CsrfViewMiddleware",
    60: "django.contrib.auth.middleware.AuthenticationMiddleware",
    70: "django.contrib.messages.middleware.MessageMiddleware",
    80: "django.middleware.clickjacking.XFrameOptionsMiddleware",
    90: "django.contrib.sites.middleware.CurrentSiteMiddleware",
}
if PROFILING:
    MIDDLEWARE_ORDERED[71] = "silk.middleware.SilkyMiddleware"
    SILKY_PYTHON_PROFILER = True
    SILKY_PYTHON_PROFILER_BINARY = True


MIDDLEWARE = [mw for _, mw in sorted(MIDDLEWARE_ORDERED.items())]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [PROJECT_DIR / "jinja2",],  # где искать шаблоны
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

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
# ]

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

STATIC_ROOT = (
    REPO_DIR / ".static"
)  # куда соберется вся статика после команды collectstatic - папка создается.
# в джанге куча статики в разных местах и разных приложениях

if not DEBUG:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=_settings.SENTRY_DSN,
        integrations=[DjangoIntegration()],
        send_default_pii=True,
    )

EMAIL_HOST = _settings.EMAIL_HOST
EMAIL_HOST_PASSWORD = _settings.EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = _settings.EMAIL_HOST_USER
EMAIL_PORT = _settings.EMAIL_PORT
EMAIL_USE_SSL = _settings.EMAIL_USE_SSL
EMAIL_USE_TLS = _settings.EMAIL_USE_TLS

EMAIL_FROM = _settings.EMAIL_FROM

LOGIN_URL = reverse_lazy("onboarding:sign_in")
LOGIN_REDIRECT_URL = reverse_lazy("onboarding:me")

SITE_ID = _settings.SITE_ID
