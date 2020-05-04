from django.db import models as m


class Resume(m.Model):
    title = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    experience = m.ManyToManyField("Experience", related_name="resume", blank=True)
    user = m.ForeignKey("users.User", on_delete=m.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.title}"
