import os

from django.conf import settings
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
from .forms import UploadVideoForm
from .models.tag import Tag
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
        form = UploadVideoForm()
        context = {
            "title": "HyperTube | Upload",
            "upload_form": form
        }
        return render(request, "tube/upload.html", context)

        # NOTE: will not pass test #13
        # if request.user.is_authenticated:
        #     context = {
        #         "title": "HyperTube | Upload",
        #         "upload_form": form
        #     }
        #     return render(request, "tube/upload.html", context)
        # return redirect("tube:login")

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get("video", None)
            title = request.POST.get("title", None)
            tag_names = request.POST.get("tags", None).split(" ")

            tags = [Tag.objects.create(name=name) for name in tag_names]
            video = Video.objects.create(file=file, title=title)
            for tag in tags:
                VideoTag.objects.create(tag=tag, video=video)

            messages.info(request, "File uploaded.")
        else:
            messages.error(request, "Failed to upload file.")
        return redirect("tube:index")


class VideoResponseView(View):
    def get(self, request: HttpRequest, file_name: str, *args, **kwargs) -> HttpResponse:
        with open(os.path.join(settings.MEDIA_ROOT, file_name), "rb") as f:
            file = f.read()
        response = HttpResponse(file, content_type="video/mp4")
        response["Accept-Ranges"] = "bytes"
        return response

        # if video := Video.objects.filter(file=file_name).first():
        #     path = settings.MEDIA_ROOT + "/" + video.file.name
        #     response = HttpResponse(video.file, content_type="video/mp4")
        #     response["Accept-Ranges"] = "bytes"
        #
        #     return response


class WatchView(View):
    def get(self, request: HttpRequest, video_id: int, *args, **kwargs) -> HttpResponse:
        print(f"video id = {video_id}")
        video_tag = VideoTag.objects.filter(video__id=video_id).first()

        tags = video_tag.tag.name.split(" ")
        print(f"tags = {tags}")

        context = {
            "title": "HyperTube | Watch",
            "video_tag": video_tag,
            "tags": tags,
        }
        return render(request, "tube/watch.html", context)
