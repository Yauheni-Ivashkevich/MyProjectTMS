from datetime import timedelta
from os import urandom

import delorean
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.test import TestCase

from apps.onboarding.models import AuthProfile
from project.utils.xdatetime import utcnow

User = get_user_model()


class Test(TestCase):
    def test_auth_profile(self):
        placeholder = urandom(4).hex()
        user = User.objects.create_user(username=placeholder, email=placeholder)

        auth = AuthProfile(user=user, verification_code=placeholder)
        auth.save()
        self.assertTrue(auth.pk)
        self.assertFalse(auth.is_verified)
        self.assertFalse(auth.link)

        auth.verified_at = delorean.parse("2020-01-01").datetime
        auth.save()
        self.assertTrue(auth.is_verified)
        self.assertFalse(auth.link)

        auth.verified_at = utcnow() + timedelta(minutes=1)
        auth.save()
        self.assertFalse(auth.is_verified)
        self.assertFalse(auth.link)

        auth.site = Site.objects.first()
        auth.save()
        self.assertFalse(auth.is_verified)
        self.assertTrue(auth.link)

        auth.verified_at = utcnow() - timedelta(seconds=1)
        auth.save()
        self.assertTrue(auth.is_verified)
        self.assertTrue(auth.link)

        self.assertEqual(
            str(auth), f"AuthProfile #{auth.pk} for {placeholder!r}",
        )
