from django.urls import path

from apps.onboarding.apps import OnboardingConfig
from apps.onboarding.views import IndexView
from apps.onboarding.views import PwcDoneView
from apps.onboarding.views import PwcView
from apps.onboarding.views import SignInVerifiedView
from apps.onboarding.views import SignInView
from apps.onboarding.views import SignOutView
from apps.onboarding.views import SignUpConfirmedView
from apps.onboarding.views import SignUpView
from apps.onboarding.views.profile import ProfileView
from apps.onboarding.views.profile_edit import ProfileEditView

app_name = OnboardingConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("me/", ProfileView.as_view(), name="me"),
    path("me/edit/", ProfileEditView.as_view(), name="me_edit"),
    path("pwc/", PwcView.as_view(), name="pwc"),
    path("pwc/done/", PwcDoneView.as_view(), name="pwc_done",),
    path("sign_in/", SignInView.as_view(), name="sign_in",),
    path("sign_in/<str:code>/", SignInVerifiedView.as_view(), name="sign_in_verified",),
    path("sign_out/", SignOutView.as_view(), name="sign_out",),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("sign_up/confirmed/", SignUpConfirmedView.as_view(), name="sign_up_confirmed"),
]
