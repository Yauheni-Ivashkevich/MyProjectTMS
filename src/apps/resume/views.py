from django.views.generic import TemplateView

from apps.resume.models import Resume


class IndexView(TemplateView):
    template_name = "resume/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        resume = Resume.objects.first()

        ctx = {
            "title": resume.title,
            "description": resume.description,
            "name": resume.user.name,
            "experiences": resume.experience.all()
        }

        ctx.update(parent_ctx)

        return ctx
