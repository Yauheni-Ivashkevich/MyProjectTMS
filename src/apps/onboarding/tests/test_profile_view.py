from django.test import TestCase

from apps.onboarding.views.profile import ProfileView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/o/me/",
            expected_view_name="onboarding:me",
            expected_view=ProfileView,
            expected_template="onboarding/me.html",
        )
