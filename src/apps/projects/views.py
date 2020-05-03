from django.views.generic import TemplateView

from apps.projects.models import Project


class IndexView(TemplateView):
    template_name = "projects/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        projects = Project.objects.all()

        ctx = {"projects": projects}

        ctx.update(parent_ctx)

        return ctx
