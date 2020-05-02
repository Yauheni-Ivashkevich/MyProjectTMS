from django.urls import path

from apps.thoughts.apps import ThoughtsConfig
from apps.thoughts.views import IndexView

app_name = ThoughtsConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
