from django.views.generic import TemplateView

from apps.index.models import UserInfo


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = UserInfo.objects.first()

        if info:
            ctx = {"name": info.name, "greeting": info.greeting, "age": info.age}
        else:
            ctx = { "name": "", "greeting": "", "age": "" }

        ctx.update(parent_ctx)

        return ctx
