from django.urls import path
from django.views.generic import RedirectView

from .views import IndexView
from .views import LoginView
from .views import LogoutView
from .views import RegisterView
from .views import UploadView
from .views import WatchView
from .views import VideoResponseView

app_name = "tube"
urlpatterns = [
    path("", RedirectView.as_view(url="tube/")),
    path("tube/", IndexView.as_view(), name="index"),
    path("tube/upload/", UploadView.as_view(), name="upload"),

    path("tube/<str:file_name>", VideoResponseView.as_view(), name="video"),
    path("tube/watch/<int:video_id>/", WatchView.as_view(), name="watch"),

    path("login", RedirectView.as_view(url="login/")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", RegisterView.as_view(), name="register"),
]
