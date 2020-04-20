from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.index.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdminModel(ModelAdmin):
    pass


# Register your models here.
