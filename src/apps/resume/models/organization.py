from django.db import models


class Organization(models.Model):
    name = models.TextField(unique=True)
    link = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.pk})"

    class Meta:
        ordering = ("name",)
