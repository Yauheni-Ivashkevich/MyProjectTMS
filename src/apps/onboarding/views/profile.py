from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()


class ProfileView(TemplateView):
    template_name = "onboarding/me.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        req = self.request

        try:
            profile = req.user.profile
        except (User.profile.RelatedObjectDoesNotExist, AttributeError):
            profile = None

        ctx["profile"] = profile

        newbie = (req.GET or {}).get("newbie")
        if newbie:
            ctx["newbie_alert"] = " ".join(
                (
                    "We strongly encourage you to update your profile and password!",
                    "Your current password is the same as your current username.",
                    "Please copy the username, set the new one, and update the password.",
                )
            )

        return ctx
