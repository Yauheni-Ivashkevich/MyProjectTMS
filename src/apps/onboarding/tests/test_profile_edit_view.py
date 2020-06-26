import contextlib

from django.test import Client
from django.test import TestCase

from apps.onboarding.views import ProfileEditView
from apps.onboarding.views import ProfileView
from project.utils.xtests import TemplateResponseTestMixin
from project.utils.xtests import UserTestMixin


class Test(TestCase, TemplateResponseTestMixin, UserTestMixin):
    def test_get_anonymous(self):
        self.validate_response(
            url="/o/me/edit/",
            expected_view_name="onboarding:me_edit",
            expected_view=ProfileEditView,
            expected_template="onboarding/me_edit.html",
            content_filters=(lambda _c: b"not authorized" in _c,),
        )

    def test_get_normal_user(self):
        user = self.create_user(verified=True)
        client = Client()
        client.login(username=user.username, password=user.username)

        self.validate_response(
            client=client,
            url="/o/me/edit/",
            expected_view_name="onboarding:me_edit",
            expected_view=ProfileEditView,
            expected_template="onboarding/me_edit.html",
            content_filters=(
                lambda _c: b"not authorized" not in _c,
                lambda _c: user.username.encode() in _c,
            ),
        )

    def test_profile_update(self):
        with self._generic_case_with_user_setup():
            pass

    def test_absent_profile_update(self):
        with self._generic_case_with_user_setup() as user:
            profile = user.profile
            profile.delete()
            user.refresh_from_db()

    @contextlib.contextmanager
    def _generic_case_with_user_setup(self):
        user = self.create_user(verified=True)

        yield user

        client = Client()
        client.login(username=user.username, password=user.username)

        new_username = f"username_{user.username}_xxx"
        new_name = f"name_{user.username}_xxx"

        self.validate_response(
            client=client,
            url="/o/me/edit/",
            method="post",
            form_data={"username": new_username, "name": new_name},
            expected_view_name="onboarding:me",
            expected_view=ProfileView,
            expected_template="onboarding/me.html",
            content_filters=(
                lambda _c: b"not authorized" not in _c,
                lambda _c: new_name.encode() in _c,
                lambda _c: new_username.encode() in _c,
            ),
        )

        user.refresh_from_db()
        self.assertEqual(user.username, new_username)

        profile = user.profile
        profile.refresh_from_db()
        self.assertEqual(profile.name, new_name)
