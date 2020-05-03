from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.resume.models import Job
from apps.resume.models import Experience
from apps.resume.models import Resume
from project.utils.xforms import gen_textinput_admin_form


@admin.register(Job)
class JobAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Job, (
            Job.name,
            Job.description,
            Job.area,
        ),
    )


@admin.register(Experience)
class JobAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Experience, (
            Experience.position,
            Experience.started_at,
            Experience.finished_at,
            Experience.responsibilities,
        ),
    )


@admin.register(Resume)
class ResumeAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Resume, (
            Resume.title,
            Resume.description,
            Resume.experience,
            Resume.user,
        ),
    )
