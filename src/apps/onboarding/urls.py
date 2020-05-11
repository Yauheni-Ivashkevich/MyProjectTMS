from django.urls import path

from apps.onboarding.views import SignUpView

urlpatterns = [path("signup/", SignUpView.as_view(), name="signup")]
