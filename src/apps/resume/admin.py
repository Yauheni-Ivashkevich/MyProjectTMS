from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Technology
from apps.resume.models import Project


@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    pass
