from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadVideoForm(forms.Form):
    video = forms.FileField(label="Select a video:")
    title = forms.CharField(label="Title:")
    tags = forms.CharField(label="Point tags:")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user
