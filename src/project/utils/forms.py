from typing import Iterable

from django import forms
from django.db import models

from project.utils.xmodels import a


def gen_textinput_admin_form(
    model_cls: type, model_fields: Iterable[models.Field]
) -> type:
    model_field_names = (a(_field) for _field in model_fields)

    class AdminFormWithTextInputs(forms.ModelForm):
        class Meta:
            model = model_cls
            fields = "__all__"
            widgets = {
                _field: forms.TextInput(attrs={"size": "100"})
                for _field in model_field_names
            }

    return AdminFormWithTextInputs
