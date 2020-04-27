from django.db import models


class Framework(models.Model):
    name = models.TextField()
    version = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        version = f" {self.version}" if self.version else ""
        return f"{self.name}{version}"

    class Meta:
        ordering = ("name",)
        constraints = (
            models.UniqueConstraint(
                fields=("name", "version"), name="unique_name_version_v01"
            ),
        )
