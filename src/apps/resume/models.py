from django.db import models as m

from project.utils.xdatetime import DateDelta
from project.utils.xdatetime import utcnow


class ResumePage(m.Model):
    title = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Resume Page"

    def __str__(self):
        return f"ResumePage [id_{self.pk}]"


class Organization(m.Model):
    name = m.TextField(null=True, blank=True)
    position = m.TextField(null=True, blank=True)
    started_at = m.DateField(null=True, blank=True)
    finished_at = m.DateField(null=True, blank=True)
    achievements_text = m.TextField(null=True, blank=True)
    link = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Organizations"

    def __str__(self):
        return f"{self.name} [id_{self.pk}]"


class Responsibility(m.Model):
    summary = m.TextField()
    organization = m.ForeignKey(
        Organization, on_delete=m.CASCADE, related_name="responsibilities"
    )

    class Meta:
        verbose_name_plural = "Responsibilities"

    def __str__(self):
        return f"Responsibility [id_{self.pk}]"
