from django.urls import reverse_lazy
from django.views.generic import RedirectView

from apps.onboarding.utils.verification import finalize_verification


class SignInVerifiedView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        code = self.kwargs.get("code")
        verified = finalize_verification(self.request, code)

        if not verified:
            url = reverse_lazy("onboarding:sign_in")
        else:
            url = reverse_lazy("onboarding:me") + "?newbie=1"

        return url
