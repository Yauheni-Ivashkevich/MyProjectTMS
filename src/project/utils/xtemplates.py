from typing import Dict
from typing import Optional

import jinja2
from django.conf import settings
from django.http import HttpRequest
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

from project.utils import consts
from project.utils.xdatetime import get_user_hour


def user_hour(request: HttpRequest) -> Dict[str, int]:
    hour = get_user_hour(request)
    ctx = {
        "user_hour": hour,
        "daylight_hours": consts.DAYLIGHT,
    }

    return ctx


def build_jinja2_environment(**options) -> Environment:
    opts = options.copy()

    opts.update(
        {
            "auto_reload": True,
            "undefined": (
                jinja2.DebugUndefined if settings.DEBUG else jinja2.ChainableUndefined
            ),
        }
    )

    env = Environment(**opts)

    global_names = {
        "debug": settings.DEBUG,
        "repr": repr,
        "static": static,
        "url": reverse,
        "user_hour": user_hour,
    }

    global_names.update(big_brother())

    env.globals.update(**global_names)

    return env