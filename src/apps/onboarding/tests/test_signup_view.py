from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.onboarding.views import SignUpConfirmedView
from apps.onboarding.views import SignUpView
from project.utils.xtests import TemplateResponseTestMixin

User = get_user_model()


class Test(TestCase, TemplateResponseTestMixin):
    def test_sign_up_get(self):
        self.validate_response(
            url=f"/o/sign_up/",
            expected_view_name="onboarding:sign_up",
            expected_template="onboarding/sign_up.html",
            expected_view=SignUpView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_sign_up_post(self):
        form = {"email": "tesmail@test.com"}

        user = User.objects.filter(email=form["email"]).first()
        self.assertIsNone(user)

        self.validate_response(
            url=f"/o/sign_up/",
            method="post",
            form_data=form,
            expected_view_name="onboarding:sign_up_confirmed",
            expected_template="onboarding/sign_up_confirmed.html",
            expected_view=SignUpConfirmedView,
            expected_redirect_chain=[("/o/sign_up/confirmed/", 302)],
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

        user = User.objects.get(email=form["email"])
        self.assertIsNotNone(user)
        self.assertFalse(user.is_active)
