from django.db import models


class Technology(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"#{self.pk} : name={self.name!r})"


class Project(models.Model):
    started_ad = models.DateField(null=True, blank=True)
    finished_ad = models.DateField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")



