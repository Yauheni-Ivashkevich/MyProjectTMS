from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from project.utils.static import render_static, resolve_static_path

class IndexView(TemplateView):
    template_name = "index/index.html"

# class StylesView(TemplateView):
#     template_name = "index/styles.css"
