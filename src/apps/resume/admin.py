from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Organization
from apps.resume.models import Responsibility
from apps.resume.models import ResumePage
from project.utils.forms import gen_textinput_admin_form


@admin.register(ResumePage)
class ResumePageAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        ResumePage, (ResumePage.title, ResumePage.description)
    )


@admin.register(Organization)
class OrganizationAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Organization, (Organization.name, Organization.position)
    )


@admin.register(Responsibility)
class ResponsibilityAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Responsibility, (Responsibility.summary,)
    )

