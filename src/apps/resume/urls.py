from django.urls import path

from apps.resume.views import IndexView

app_name = ResumeConfig.name

urlpatterns = [
    path('resume/', IndexView.as_view(), name="resume"),
]
