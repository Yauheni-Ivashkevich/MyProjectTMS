from django.contrib.auth import get_user_model
from django.db import models as m
from django.urls import reverse_lazy

User = get_user_model()
# лучше всего использовать такой способ модели юзера


class FeedbackPost(m.Model):
    author = m.ForeignKey(User, on_delete=m.SET_NULL, null=True, blank=True)
    title = m.TextField(null=True, blank=True)
    preview = m.TextField(null=True, blank=True)
    content = m.TextField(null=True, blank=True)
    # CASCADE - при удалении пользователя удаляются и его посты
    # SET_NULL - обнуляет ключевые поля при удалении юзера

    def get_absolute_url(self):
        return reverse_lazy("feedback:post", kwargs={"pk": str(self.pk)})
