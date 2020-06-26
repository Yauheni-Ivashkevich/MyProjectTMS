from django.core.files.storage import FileSystemStorage
from django.test import TestCase
from rest_framework import status

from applications.meta.applications.blog.models import Photo
from applications.meta.applications.blog.models import Post
from project.utils.xtests import ApiTestMixin
from project.utils.xtests import UserTestMixin


class Test(TestCase, ApiTestMixin, UserTestMixin):
    def setUp(self) -> None:
        self.endpoint = "/api/v1/photo/"
        self.user = self.create_user()
        self.token = self.create_auth_token(self.user)
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        self.blog_post = Post()
        self.blog_post.save()
        Photo.original.field.storage = FileSystemStorage()
        Photo.thumbnail.field.storage = FileSystemStorage()
        self.photo = Photo(post=self.blog_post, original="xxx")
        self.photo.save()

    def test_user_anon(self):
        self.validate_response(
            self.endpoint, expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_user_normal(self):
        self.validate_response(
            self.endpoint,
            headers=self.auth_headers,
            expected_response_payload=[
                {
                    "original": f"http://testserver/api/v1/photo/{self.photo.original.url}",
                    "post": self.blog_post.pk,
                    "thumbnail": "",
                    "uuid": str(self.photo.pk),
                },
            ],
        )

    def test_post_anon(self):
        self.validate_response(
            self.endpoint,
            method="post",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )
