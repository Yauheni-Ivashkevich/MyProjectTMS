from os import urandom
from unittest import TestCase

from django.contrib.auth import get_user_model

from apps.onboarding.forms.profile_edit import ProfileEditForm
from apps.onboarding.forms.sign_up import SignUpForm
from project.utils.xtests import UserTestMixin

User = get_user_model()


class Test(TestCase, UserTestMixin):
    def test_sign_up_form_empty(self):
        form = SignUpForm({})
        with self.assertRaises(ValueError):
            form.save()

    def test_sign_up_form_bad_email(self):
        form = SignUpForm({"email": ""})
        with self.assertRaises(ValueError):
            form.save()

        form = SignUpForm({"email": "xxx"})
        with self.assertRaises(ValueError):
            form.save()

    def test_sign_up_form_email_taken(self):
        user = self.create_user()

        form = SignUpForm({"email": user.email})
        with self.assertRaises(ValueError):
            form.save()

    def test_sign_up_form_success(self):
        placeholder = urandom(4).hex()
        email = f"email_{placeholder}@test.com"

        form = SignUpForm({"email": email})
        form.save()

        user = User.objects.filter(email=email)
        self.assertEqual(user.count(), 1)

        user = user.first()
        self.assertEqual(email, user.email)
        self.assertTrue(user.username)
        self.assertTrue(user.check_password(user.username))

    def test_profile_edit_form_empty(self):
        form = ProfileEditForm({})
        self.assertFalse(form.is_valid())

    def test_profile_edit_form_bad_username(self):
        form = ProfileEditForm({"username": ""})
        self.assertFalse(form.is_valid())

    def test_profile_edit_form_username_taken(self):
        user = self.create_user()

        form_data = {"username": user.username}

        form = ProfileEditForm(form_data)
        self.assertFalse(form.is_valid())

        form = ProfileEditForm(form_data, initial=form_data)
        self.assertTrue(form.is_valid())

        new_form_data = form_data.copy()
        new_form_data["username"] *= 2

        form = ProfileEditForm(new_form_data, initial=form_data)
        self.assertTrue(form.is_valid())

        new_form_data = form_data.copy()
        new_form_data["name"] = "xxx"

        form = ProfileEditForm(new_form_data, initial=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_edit_form_success(self):
        placeholder = urandom(4).hex()
        form_data = {"username": placeholder}

        form = ProfileEditForm(form_data)
        self.assertTrue(form.is_valid())
