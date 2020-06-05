from django.contrib.auth.views import PasswordChangeDoneView


class PwcDoneView(PasswordChangeDoneView):
    template_name = "onboarding/pwc_done.html"
