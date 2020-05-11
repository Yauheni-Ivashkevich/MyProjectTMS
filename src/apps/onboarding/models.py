# from typing import Optional
#
# from django.contrib.auth import get_user_model
# from django.contrib.sites.models import Site
# from django.db import models
# from django.urls import reverse_lazy
#
# from project.utils.xdatetime import utcnow
#
# User = get_user_model()
#
#
# class AuthProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     verification_code = models.CharField(max_length=255, unique=True)
#     verified_at = models.DateTimeField(null=True, blank=True)
#     notified_at = models.DateTimeField(null=True, blank=True)
#     site = models.ForeignKey(
#         Site, null=True, blank=True, on_delete=models.CASCADE, db_index=True
#     )
#
#     @property
#     def is_verified(self) -> bool:
#         cond = self.verified_at and self.verified_at <= utcnow()
#         return cond
#
#     @property
#     def link(self) -> Optional[str]:
#         if not self.site:
#             return None
#
#         domain = self.site.domain
#         scheme = {"localhost": "http"}.get(domain, "https")
#
#         url = f"{scheme}://{domain}{self.get_absolute_url()}"
#
#         return url
#
#     def get_absolute_url(self) -> str:
#         return reverse_lazy(
#             "onboarding:sign_in_verified", kwargs={"code": self.verification_code}
#         )
#
#     def __str__(self) -> str:
#         return f"{self.__class__.__name__} #{self.pk} for {self.user.email!r}"
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, primary_key=True, related_name="profile"
#     )
#     name = models.TextField(null=True, blank=True)
#
#     def __str__(self) -> str:
#         return f"{self.__class__.__name__} #{self.pk} for {self.user.email!r}"
