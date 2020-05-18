from django.test import TestCase

from apps.resume.views import IndexView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/resume/",
            expected_view=IndexView,
            expected_view_name="resume:index",
            expected_template="resume/index.html",
        )