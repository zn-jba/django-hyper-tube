from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        videos = ...
        return render(request, "tube/index.html", {"videos": videos})


class LoginView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/login.html")


class UploadView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/upload.html")
