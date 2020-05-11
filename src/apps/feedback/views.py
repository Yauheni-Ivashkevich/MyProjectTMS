from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

from apps.feedback.models import FeedbackPost


class AllFeedbackPostsView(ListView):  # mix сюда
    template_name = "all_posts.html"
    model = FeedbackPost


class FeedbackPostView(DetailView):
    template_name = "post.html"
    model = FeedbackPost
