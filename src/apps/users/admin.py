from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.users.models import User

from project.utils.xforms import gen_textinput_admin_form


@admin.register(User)
class UserAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        User, (
            User.name,
            User.birthday,
            User.about,
        ),
    )

