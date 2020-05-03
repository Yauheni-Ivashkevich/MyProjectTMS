from django.db import models as m
from project.utils.xdatetime import DateDelta
from project.utils.xdatetime import utcnow

# Create your models here.


class Project(m.Model):
    name = m.TextField(null=True, blank=True)
    link = m.TextField(null=True, blank=True)
    linkName = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    gallery = m.TextField(null=True, blank=True)
    sponsor = m.TextField(null=True, blank=True)
    sponsorLogo = m.TextField(null=True, blank=True)
    started_at = m.DateField(default=utcnow)
    finished_at = m.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def duration(self) -> DateDelta:
        delta = DateDelta.build(self.started_at, self.finished_at)
        return delta
