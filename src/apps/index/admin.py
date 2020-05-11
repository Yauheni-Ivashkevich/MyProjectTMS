from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.index.models import MainPage
from apps.index.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(MainPage)
class MainPageAdminModel(ModelAdmin):
    pass
