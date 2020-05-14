from os import urandom
from unittest import skip

from django.test import Client
from django.test import TestCase

from apps.feedback.models import FeedbackPost
from apps.feedback.views import AllFeedbackPostsView, FeedbackPostView
from project.utils.user_utils import UserTestMixin
from project.utils.validate_response import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):

    def test_get(self):
        self.validate_response(
            url="/feedback/",
            expected_view=AllFeedbackPostsView,
            expected_template="feedback/post.html",
            expected_view_name="feedback:post",
        )

    def test_post(self):
        self.validate_response(
            method="post",
            url="/feedback/",
            expected_status_code=405,
            expected_view=AllFeedbackPostsView,
            expected_template="feedback/all_posts.html",
            expected_view_name="feedback:all_posts",
        )

    def test_get_absent(self):
        self.validate_response(
            url="/feedback/post/01/",
            expected_status_code=404,
            expected_view=FeedbackPostView,
            expected_template="feedback/post.html",
            expected_view_name="feedback:post",
        )

    def test_get_existing_anon(self):
        placeholder = urandom(4).hex()
        post = FeedbackPost(title=placeholder, content=placeholder)
        post.save()

        self.validate_response(
            url=f"/feedback/post/{post.pk}/",
            expected_view=FeedbackPostView,
            expected_template="feedback/post.html",
            expected_view_name="feedback:post",
        )

    def test_get_existing_authed(self):
        placeholder = urandom(4).hex()
        user = self.create_user(placeholder)
        client = Client()
        client.login(username=user.username, password=placeholder)

        post = FeedbackPost(title=placeholder, content=placeholder)
        post.save()

        self.validate_response(
            client=client,
            url=f"/feedback/post/{post.pk}/",
            expected_view=FeedbackPostView,
            expected_template="feedback/post.html",
            expected_view_name="feedback:post",
        )

    def test_post(self):
        post = FeedbackPost()
        post.save()

        self.validate_response(
            method="post",
            url=f"/feedback/post/{post.pk}/",
            expected_status_code=405,
            expected_view=FeedbackPostView,
            expected_template="feedback/post.html",
            expected_view_name="feedback:post",
        )