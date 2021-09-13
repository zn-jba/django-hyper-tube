from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from .models.video import Video

VIDEOS = [
    {
        "id": 0,
        "link": "#",
        "title": "Introduction To Python",
    },
    {
        "id": 1,
        "link": "#",
        "title": "My football training",
    },
    {
        "id": 2,
        "link": "#",
        "title": "Surfing tour",
    },
    {
        "id": 3,
        "link": "#",
        "title": "Football match as a spectator",
    },
]


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        videos = Video.find_all() or VIDEOS
        return render(request, "tube/index.html", {"videos": videos})


class LoginView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/login.html")


class UploadView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/upload.html")
