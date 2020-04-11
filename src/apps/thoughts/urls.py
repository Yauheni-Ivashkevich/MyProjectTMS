from django.urls import path

from apps.thoughts.views import IndexView
from apps.thoughts.apps import ThoughtsConfig

app_name = ThoughtsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
