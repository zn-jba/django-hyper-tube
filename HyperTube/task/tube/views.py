from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import RegisterForm
from .models.video import Video
from .models.video_tag import VideoTag


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if tag := request.GET.get("tag", None):
            video_tags = VideoTag.objects.filter(tag__name__iexact=tag)
            videos = [video_tag.video for video_tag in video_tags]
        elif query := request.GET.get("q", None):
            video_tags = VideoTag.objects.filter(video__title__icontains=query)
            videos = [vt.video for vt in video_tags]
        else:
            videos = Video.find_all()

        context = {
            "videos": videos or None,
            "tag": tag or None,
            "title": "HyperTube | Home"
        }
        return render(request, "tube/index.html", context)


class LoginView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = AuthenticationForm()
        return render(request, "tube/login.html", {"login_form": form})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username", None)
            password = form.cleaned_data.get("password", None)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("tube:index")
        messages.error(request, "Invalid credentials.")
        return redirect("tube:login")


class LogoutView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("tube:index")


class RegisterView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = RegisterForm()
        return render(request, "tube/register.html", {"register_form": form})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successfully signed up.")
            return redirect("tube:login")
        messages.error(request, "Invalid credentials.")
        return redirect("tube:register")


class UploadView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "tube/upload.html", {"title": "HyperTube | Upload"})
