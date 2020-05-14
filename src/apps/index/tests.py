from os import urandom
from unittest import skip

from django.test import TestCase

from apps.index.models import MainPage
from apps.index.models import UserInfo
from apps.index.views import IndexView
from project.utils.validate_response import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/",
            expected_view_name="index:index",
            expected_view=IndexView,
            expected_template="index/index.html",
        )

    def test_userinfo(self):
        placeholder = urandom(4).hex()
        userinfo = UserInfo(name=placeholder)
        self.assertEqual(
            str(userinfo), f"UserInfo(id={userinfo.pk}, name={placeholder!r})"
        )

    def test_mainpage(self):
        placeholder = urandom(4).hex()
        mainpage = MainPage(title=placeholder)
        self.assertEqual(str(mainpage), f"MainPage(id={mainpage.pk})")