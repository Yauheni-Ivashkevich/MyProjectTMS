from os import urandom

from django import forms
from django.contrib.auth import get_user_model

from project.utils.xmodels import a

User = get_user_model()


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, min_length=1, required=True)

    class Meta:
        model = User
        fields = [a(User.email)]

    def clean(self):
        super().clean()

        email = self.cleaned_data.get("email")
        if not email:
            self.add_error("email", f"E-mail is required.")
        else:
            if User.objects.filter(email=email).exists():
                self.add_error("email", f"E-mail {email} is already taken.")

    def save(self, commit=True):
        if self.errors:
            return super().save(commit)

        rs = urandom(16).hex()
        user = User.objects.create_user(
            email=self.cleaned_data["email"], is_active=False, password=rs, username=rs,
        )
        return user
