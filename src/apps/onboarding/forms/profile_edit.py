from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    name = forms.CharField(max_length=1000, required=False)

    def clean_username(self):
        cleaned = self.cleaned_data["username"]

        if not self.has_changed():
            return cleaned

        if "username" not in self.changed_data:
            return cleaned

        if User.objects.filter(username=cleaned).count():
            raise forms.ValidationError("Username has been already taken")

        return cleaned
