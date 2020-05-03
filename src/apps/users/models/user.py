from django.db import models as m


class User(m.Model):
    name = m.TextField(null=True, blank=True)
    birthday = m.DateField(null=True, blank=True)
    about = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        x = "User"
        return f"User(id={self.pk}, name={self.name!r})"
