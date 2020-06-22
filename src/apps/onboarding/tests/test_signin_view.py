from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.onboarding.views import SignInView
from apps.onboarding.views.profile import ProfileView
from project.utils.xtests import TemplateResponseTestMixin
from project.utils.xtests import UserTestMixin

User = get_user_model()


class Test(TestCase, TemplateResponseTestMixin, UserTestMixin):
    def test_sign_in_get(self):
        self.validate_response(
            url=f"/o/sign_in/",
            expected_view_name="onboarding:sign_in",
            expected_template="onboarding/sign_in.html",
            expected_view=SignInView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_sign_in_post_success(self):
        user = self.create_user()

        form_data = {
            "username": user.username,
            "email": user.email,
            "password": user.username,
        }

        self.validate_response(
            url=f"/o/sign_in/",
            method="post",
            form_data=form_data,
            expected_view_name="onboarding:me",
            expected_template="onboarding/me.html",
            expected_view=ProfileView,
            expected_redirect_chain=[("/o/me/", 302)],
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_sign_in_post_failure_bad_creds(self):
        user = self.create_user()

        form_data = {
            "username": user.username,
            "email": user.email,
            "password": user.username * 2,
        }

        self.validate_response(
            url=f"/o/sign_in/",
            method="post",
            form_data=form_data,
            expected_view_name="onboarding:sign_in",
            expected_template="onboarding/sign_in.html",
            expected_view=SignInView,
            content_filters=(lambda _c: b"error" in _c,),
        )

    def test_signin_verified_success(self):
        user = self.create_user(verified=True)

        self.validate_response(
            url=f"/o/sign_in/{user.username}/",
            expected_view_name="onboarding:me",
            expected_template="onboarding/me.html",
            expected_view=ProfileView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
            expected_redirect_chain=[("/o/me/?newbie=1", 302)],
        )

    def test_signin_verified_failure_bad_code(self):
        user = self.create_user(verified=True)

        self.validate_response(
            url=f"/o/sign_in/{user.username * 2}/",
            expected_view_name="onboarding:sign_in",
            expected_template="onboarding/sign_in.html",
            expected_view=SignInView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_signin_verified_failure_not_verified(self):
        user = self.create_user()

        self.validate_response(
            url=f"/o/sign_in/{user.username}/",
            expected_view_name="onboarding:sign_in",
            expected_template="onboarding/sign_in.html",
            expected_view=SignInView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )
