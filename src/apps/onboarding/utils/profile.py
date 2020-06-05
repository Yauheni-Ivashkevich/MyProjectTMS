from typing import Union

from django.contrib.auth import get_user_model

from apps.onboarding.models import Profile

User = get_user_model()


def setup_profile(user: User) -> Union[Profile, None]:
    if not user or not user.is_authenticated:
        return None

    profile = Profile.objects.filter(user=user)

    if not profile.count():
        profile = Profile(user=user)
        profile.save()
        profile = Profile.objects.filter(user=user)

    return profile.first()
