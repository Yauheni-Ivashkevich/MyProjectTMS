from django.views.generic import ListView

from apps.resume.models import Project


class IndexView(ListView):
    template_name = "resume/index.html"
    queryset = Project.objects.filter(is_hidden=False)




