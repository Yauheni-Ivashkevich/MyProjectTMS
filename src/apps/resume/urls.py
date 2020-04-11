from django.urls import path

from apps.index.apps import IndexConfig
from apps.resume.views import IndexView

app_name = IndexConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
