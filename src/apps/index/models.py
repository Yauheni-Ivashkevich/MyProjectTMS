from django.db import models as m

# Create your models here.


class UserInfo(m.Model):
    name = m.TextField(
        unique=True
    )  # требование уникальности при вводе и нельзя ничего не вводит
    greeting = m.TextField(null=True, blank=True)
    age = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User Info"

    def __str__(self):
        x = "UserInfo"
        return f"UserInfo(id={self.pk}, name={self.name!r})"
