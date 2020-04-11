from django.urls import path

from apps.projects.apps import ProjectsConfig
from apps.projects.views import IndexView

app_name = ProjectsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
