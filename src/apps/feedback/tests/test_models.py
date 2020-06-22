from unittest import TestCase

from apps.feedback.models import Comment
from apps.feedback.models import Post
from project.utils.xtests import UserTestMixin


class Test(TestCase, UserTestMixin):
    def test_post_model(self):
        post = Post()
        post.save()

        self.assertEqual(f"/feedback/posts/{post.pk}/", post.get_absolute_url())
        self.assertIsNone(None, post.nr_likes)
        self.assertIsNone(None, post.nr_dislikes)

        post.upvote()
        self.assertEqual(1, post.nr_likes)
        post.upvote()
        self.assertEqual(2, post.nr_likes)

        post.downvote()
        self.assertEqual(1, post.nr_dislikes)
        post.downvote()
        self.assertEqual(2, post.nr_dislikes)

    def test_comment(self):
        post = Post()
        post.save()
        self.assertEqual(0, post.comments.count())

        user = self.create_user()

        comment = Comment(post=post, author=user)
        comment.save()

        self.assertIsNone(None, comment.nr_likes)
        self.assertIsNone(None, comment.nr_dislikes)

        comment.upvote()
        self.assertEqual(1, comment.nr_likes)
        comment.upvote()
        self.assertEqual(2, comment.nr_likes)

        comment.downvote()
        self.assertEqual(1, comment.nr_dislikes)
        comment.downvote()
        self.assertEqual(2, comment.nr_dislikes)
