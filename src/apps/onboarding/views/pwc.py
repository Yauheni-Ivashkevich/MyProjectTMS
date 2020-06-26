from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class PwcView(PasswordChangeView):
    template_name = "onboarding/pwc_form.html"
    success_url = reverse_lazy("onboarding:pwc_done")
