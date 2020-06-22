from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.onboarding.models import Profile

User = get_user_model()


class Test(TestCase):
    def test_profile_model(self):
        user = User.objects.create_user(username="xxx", email="xxx")

        profile = Profile(user=user)
        profile.save()
        self.assertTrue(profile.pk)

        self.assertEqual(str(profile), f"Profile #{profile.pk} for 'xxx'")
