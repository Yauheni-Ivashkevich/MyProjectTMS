from django.urls import path

from apps.feedback import views
from apps.feedback.apps import FeedbackConfig

app_name = FeedbackConfig.label

urlpatterns = [
    path("", views.AllFeedbackPostsView.as_view(), name="all_posts"),
    path("post/<int:pk>/", views.FeedbackPostView.as_view(), name="post"),
    path("posts/<int:pk>/comment/", views.CommentView.as_view(), name="comment"),
]
