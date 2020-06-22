from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.impl.v1.views import PhotoViewSet

router = DefaultRouter()
router.register("photo", PhotoViewSet, "photo")

urlpatterns = [
    path("", include(router.urls)),
]
