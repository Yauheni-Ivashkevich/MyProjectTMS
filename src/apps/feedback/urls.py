from django.urls import path

from apps.feedback.apps import FeedbackConfig
from apps.feedback.views import AllFeedbackPostsView
from apps.feedback.views import FeedbackPostView

app_name = FeedbackConfig.label

urlpatterns = [
    path("", AllFeedbackPostsView.as_view(), name="all_posts"),
    path("post/<int:pk>/", FeedbackPostView.as_view(), name="post"),
]
