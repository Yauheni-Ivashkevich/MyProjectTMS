from os import urandom
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.http import HttpRequest

from apps.onboarding.models import AuthProfile
from apps.onboarding.utils import verification
from apps.onboarding.utils.profile import setup_profile

User = get_user_model()


class Test(TestCase):
    def test_setup_user_profile(self):
        placeholder = urandom(4).hex()
        user = User.objects.create_user(username=f"username_{placeholder}")
        site = Site.objects.first()
        auth = verification.setup_auth_profile(user, site)
        self.assertTrue(auth.verification_code)
        self.assertTrue(auth.link)

    def test_deactivate_user(self):
        placeholder = urandom(4).hex()
        user = User.objects.create_user(
            email=f"email_{placeholder}", username=f"username_{placeholder}",
        )
        self.assertTrue(user.is_active)

        verification.deactivate_user(user)
        self.assertFalse(user.is_active)

    def test_start_verification(self):
        request = Mock()
        request.site = Site.objects.first()

        placeholder = urandom(4).hex()

        user = User.objects.create_user(
            email=f"email_{placeholder}", username=f"username_{placeholder}",
        )
        self.assertTrue(user.is_active)
        self.assertFalse(AuthProfile.objects.filter(user=user).all())

        verification.start_verification(request, user)

        self.assertFalse(user.is_active)

        auths = AuthProfile.objects.filter(user=user)
        self.assertEqual(auths.count(), 1)

        auth = auths.first()
        self.assertTrue(auth)
        self.assertEqual(auth.user, user)
        self.assertTrue(auth.verification_code)
        self.assertTrue(auth.link)
        self.assertIsNone(auth.verified_at)
        self.assertFalse(auth.is_verified)

    @patch.object(verification, verification.login.__name__)
    def test_finalize_verification(self, mock_login):
        placeholder = urandom(4).hex()
        request = HttpRequest()

        user = User.objects.create_user(
            email=f"email_{placeholder}",
            is_active=False,
            username=f"username_{placeholder}",
        )
        user.save()

        self.assertFalse(verification.finalize_verification(request, None))
        self.assertFalse(verification.finalize_verification(request, ""))
        self.assertFalse(
            verification.finalize_verification(request, f"vc_{placeholder}")
        )

        auth = AuthProfile(user=user, verification_code=f"vc_{placeholder}")
        auth.save()

        self.assertTrue(
            verification.finalize_verification(request, f"vc_{placeholder}")
        )

        user.refresh_from_db()
        auth.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertTrue(auth.verified_at)
        mock_login.assert_called_once_with(request, user)

    def test_setup_profile(self):
        placeholder = urandom(4).hex()
        user = User.objects.create_user(username=f"username_{placeholder}")

        profile = setup_profile(None)
        self.assertFalse(profile)

        profile = setup_profile(user)
        self.assertTrue(profile)

        profile2 = setup_profile(user)
        self.assertTrue(profile2)

        self.assertEqual(profile, profile2)
