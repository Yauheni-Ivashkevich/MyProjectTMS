from django.views.generic import TemplateView

from apps.index.models import MainPage
from apps.index.models import UserInfo


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = UserInfo.objects.first()
        info_main = MainPage.objects.first()
        ctx = {
            "name": info.name,
            "greeting": info.greeting,
            "title": info_main.title,
            "description": info_main.description,
            "about": info_main.about,
        }

        ctx.update(parent_ctx)

        return ctx
