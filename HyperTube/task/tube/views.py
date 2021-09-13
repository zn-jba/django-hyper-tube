from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from .models.video import Video
from .models.video_tag import VideoTag

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
        if tag := request.GET.get("tag", None):
            video_tags = VideoTag.objects.filter(tag__name__iexact=tag)
            videos = [video_tag.video for video_tag in video_tags]
            return render(request, "tube/index.html", {"videos": videos, "tag": tag, "title": "HyperTube | Home"})

        if query := request.GET.get("q", None):
            videos = Video.objects.filter(title__icontains=query)
            # video_tags = VideoTag.objects.filter(video__title__icontains=query)
            # videos = [video_tag.video for video_tag in video_tags]
        else:
            videos = Video.find_all() or VIDEOS
        return render(request,
                      "tube/index.html",
                      {"videos": videos, "title": "HyperTube | Home"})


class LoginView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/login.html", {"title": "HyperTube | Log in"})


class UploadView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/upload.html", {"title": "HyperTube | Upload"})
