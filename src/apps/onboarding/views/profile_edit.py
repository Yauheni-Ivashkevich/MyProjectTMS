from typing import Dict

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.onboarding.forms.profile_edit import ProfileEditForm
from apps.onboarding.utils.profile import setup_profile

User = get_user_model()


class ProfileEditView(FormView):
    form_class = ProfileEditForm
    template_name = "onboarding/me_edit.html"

    def get_success_url(self):
        success_url = reverse_lazy("onboarding:me")
        return success_url

    def form_valid(self, form):
        user = self.request.user
        user.username = form.cleaned_data["username"]
        user.save()

        try:
            profile = user.profile
        except User.profile.RelatedObjectDoesNotExist:
            profile = setup_profile(user)

        profile.name = form.cleaned_data["name"]
        profile.save()

        return super().form_valid(form)

    def get_initial(self) -> Dict:
        user = self.request.user
        initial = {}

        if not user.is_anonymous:
            try:
                profile = user.profile
            except User.profile.RelatedObjectDoesNotExist:
                profile = None

            initial.update(
                {"username": user.username, "name": profile.name if profile else "",}
            )
        return initial
