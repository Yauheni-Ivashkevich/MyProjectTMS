from pathlib import Path
from django.contrib import admin

from django.http import Http404
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

from django.urls import path

here = Path(__file__).parent.resolve()

def render_static(file_path: Path, content_type: str) -> HttpResponse:
    if not file_path.is_file():
        full_path = file_path.as_posix()
        raise Http404(f"file '{full_path}' not found")

    with file_path.open("rb") as fp:
        content = fp.read()

    response = HttpResponse(content, content_type=content_type)
    return response

def resolve_static_path(path: str):
    static = here.parent.parent / 'src/project/static'
    return static / path

def view_jpg(r):
    return render_static(resolve_static_path('pic.jpg'), 'image/jpg')

def view_styles(r):
    return render_static(resolve_static_path('styles.css'), 'text/css')

def view_js(r):
    return render_static(resolve_static_path('script.js'), 'text/javascript')

def view_index(request: HttpRequest):
    return render(request, "index.html")

def view_contacts(request: HttpRequest):
    return render(request, "contacts.html")


def view_test(request: HttpRequest):
    return render(request, "test.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name="index"),
    path('contacts/', view_contacts, name="contacts"),
    path('test/', view_test, name="test"),
    path('pic.jpg', view_jpg),
    path('styles.css', view_styles),
    path('script.js', view_js),
]