from django.contrib import admin

from apps.feedback.models import Comment
from apps.feedback.models import Photo
from apps.feedback.models import Post


@admin.register(Post)
class FeedbackPostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass
