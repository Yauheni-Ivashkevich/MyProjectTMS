from django.contrib import admin

from django.http import HttpRequest
from django.shortcuts import render

from django.urls import path, include

# def read_static(fn, ct):  # fn = filename, ct = content type
#     with open(fn, "rb") as src:  # открываем объект (для картинок стоит "rb" - читать в бинарном формате
#         content = src.read()  # читаем открытый объект
#         resp = HttpResponse(content, content_type=ct)  # response
#         return resp  # выполняем
from project.utils.static import render_static, resolve_static_path
# def view_jpg(r):
#     return render_static(resolve_static_path('pic.jpg'), 'image/jpg')
# def view_resume(request: HttpRequest):
#     return render(request, "resume.html")


urlpatterns = [
    path('admin/', admin.site.urls), # позволяет входить под админом на свой сайт herokuapp.com/admin
# --- apps ---
    path('', include("apps.index.urls")),
    path('resume/', include("apps.resume.urls")),
    path('projects/', include("apps.projects.urls")),

    # path('projects/', view_projects, name="projects"),
    # path('pic.jpg', view_jpg),
    # path('styles.css', view_styles),
    # #path('script.js', view_js),
]