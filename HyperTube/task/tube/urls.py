from django.urls import path

from .views import IndexView
from .views import LoginView
from .views import UploadView

app_name = "tube"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("tube/upload/", UploadView.as_view(), name="upload"),
]
