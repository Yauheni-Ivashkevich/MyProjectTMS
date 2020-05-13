from unittest import skip

from django.test import Client
from django.test import TestCase

from apps.feedback.views import AllFeedbackPostsView, FeedbackPostView

from project.utils.validate_response import TemplateResponseTestMixin

@skip
class Test(TestCase, TemplateResponseTestMixin):

    def test_get(self):
        self.validate_response(
            url="/feedback/",
            expected_view=AllFeedbackPostsView,
            expected_template="feedback/post.html",
            expected_view_name="feedback:post",
        )


        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.templates), 2)
        self.assertEqual(
            [_t.name for _t in resp.templates], ["feedback/all_posts.html", "base.html"]
        )
        self.assertEqual(
            resp.resolver_match.func.__name__, IndexView.as_view().__name__
        )
