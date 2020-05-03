from django.db import models as m


class Job(m.Model):
    name = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    area = m.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

