from django.test import TestCase

from apps.feedback.views import AllFeedbackPostsView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/feedback/posts/",
            expected_view=AllFeedbackPostsView,
            expected_template="feedback/all_posts.html",
            expected_view_name="feedback:all_posts",
            content_filters=(lambda _c: b"feedback" in _c,),
        )

    def test_post(self):
        self.validate_response(
            method="post",
            url="/feedback/posts/",
            expected_status_code=405,
            expected_view=AllFeedbackPostsView,
            expected_template="feedback/all_posts.html",
            expected_view_name="feedback:all_posts",
            content_filters=(lambda _c: _c == b"",),
        )
