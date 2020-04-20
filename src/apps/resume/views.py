from django.views.generic import TemplateView

from apps.resume.models import Project


class IndexView(TemplateView):
    template_name = "resume/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        projects = Project.objects.all()
        ctx["projects"] = projects

        return ctx
