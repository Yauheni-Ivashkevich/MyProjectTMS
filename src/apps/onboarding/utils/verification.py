from secrets import token_urlsafe
from typing import Union

from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.sites.models import Site
from django.http import HttpRequest

from apps.onboarding.models import AuthProfile
from apps.onboarding.utils.profile import setup_profile
from project.utils import consts
from project.utils.xdatetime import utcnow

User = get_user_model()


def setup_auth_profile(user: User, site: Site) -> AuthProfile:
    code = token_urlsafe(consts.LEN_AUTH_CODE)
    auth = AuthProfile(user=user, site=site, verification_code=code)
    auth.save()
    return auth


def deactivate_user(user):
    user.is_active = False
    user.save()


def start_verification(request: HttpRequest, user: User):
    setup_auth_profile(user, request.site)
    deactivate_user(user)


def finalize_verification(request: HttpRequest, code: Union[str, None]) -> bool:
    if not code:
        return False

    try:
        auth = AuthProfile.objects.get(verification_code=code)
    except AuthProfile.DoesNotExist:
        return False

    if auth.is_verified:
        return True

    auth.verified_at = utcnow()
    auth.save()
    auth.user.is_active = True
    auth.user.save()

    setup_profile(auth.user)

    login(request, auth.user)

    return True
