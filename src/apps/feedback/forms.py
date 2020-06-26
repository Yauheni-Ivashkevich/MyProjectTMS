from django import forms

from apps.feedback.models import Comment
from project.utils.xmodels import a


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            "author": forms.HiddenInput,
            "Comment.post": forms.HiddenInput,
        }
        fields = ["author", "message", "post"]
