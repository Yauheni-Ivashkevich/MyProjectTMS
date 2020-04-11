from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "thoughts/index.html"
