from django.db import models as m

from project.utils.xdatetime import DateDelta
from project.utils.xdatetime import utcnow


# Create your models here.
class Project(m.Model):
    name = m.TextField(null=True, blank=True)
    link = m.TextField(null=True, blank=True)
    linkName = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    # gallery = m.TextField(null=True, blank=True)
    # для чего потребуется скачать $pipenv pip install Pillow (Поддержка при открытии,управлении
    # и сохранении многих форматов изображения)
    # m.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    started_at = m.DateField(default=utcnow)
    finished_at = m.DateField(null=True, blank=True)
    donor = m.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def duration(self) -> DateDelta:
        delta = DateDelta.build(self.started_at, self.finished_at)
        return delta
