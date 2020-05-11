from django.test import Client
from django.test import TestCase

from apps.projects.views import IndexView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/projects/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.has_header("Cache-Control"))
        self.assertEqual(resp.get("Cache-Control"), f"max-age={60 * 60 * 24}")

        self.assertEqual(resp.resolver_match.app_name, "projects")
        self.assertEqual(resp.resolver_match.url_name, "index")
        self.assertEqual(resp.resolver_match.view_name, "projects:index")
        self.assertEqual(
            resp.resolver_match.func.__name__, IndexView.as_view().__name__
        )

        self.assertEqual(resp.template_name, ["projects/index.html"])
