from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.feedback.models import FeedbackPost


@admin.register(FeedbackPost)
class FeedbackPostAdminModel(ModelAdmin):
    pass


