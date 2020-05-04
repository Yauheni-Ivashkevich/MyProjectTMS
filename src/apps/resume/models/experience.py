from django.db import models as m

from project.utils.xdatetime import DateDelta
from project.utils.xdatetime import utcnow


class Experience(m.Model):
    position = m.TextField(null=True, blank=True)
    started_at = m.DateField(default=utcnow)
    finished_at = m.DateField(null=True, blank=True)
    responsibilities = m.TextField(null=True, blank=True)

    experience = m.ForeignKey("Job", on_delete=m.CASCADE, related_name="resume")

    @property
    def duration(self) -> DateDelta:
        return DateDelta.build(self.started_at, self.finished_at)
