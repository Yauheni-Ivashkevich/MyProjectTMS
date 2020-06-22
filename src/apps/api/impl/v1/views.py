from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.api.impl.v1.serializers import PhotoSerializer
from apps.feedback.models import Photo


class PhotoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
