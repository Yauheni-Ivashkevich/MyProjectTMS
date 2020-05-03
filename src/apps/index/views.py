from django.views.generic import TemplateView

from apps.users.models import User


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = User.objects.first()

        if info:
            ctx = {"name": info.name, "greeting": info.about }
        else:
            ctx = { "name": "", "greeting": "" }

        ctx.update(parent_ctx)

        return ctx
