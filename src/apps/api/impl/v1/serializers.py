from django.conf import settings
from rest_framework import serializers
from rest_framework.fields import CharField

from apps.feedback.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    thumbnail = CharField()

    class Meta:
        model = Photo
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     breakpoint()
    #     return super().update(instance, validated_data)

    # @staticmethod
    # def validate_thumbnail(value):
    #     url = f"https://s3.amazonaws.com" \
    #           f"/{settings.AWS_STORAGE_BUCKET_NAME}" \
    #           f"/{settings.AWS_LOCATION}" \
    #           f"/{value}"
    #     return url
