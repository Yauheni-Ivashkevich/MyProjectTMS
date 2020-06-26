from django.views.generic import TemplateView


class SignUpConfirmedView(TemplateView):
    template_name = "onboarding/sign_up_confirmed.html"
