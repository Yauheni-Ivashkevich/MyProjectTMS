from django.urls import path

from apps.projects.apps import ProjectsConfig
from apps.projects.views import IndexView

app_name = ProjectsConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
