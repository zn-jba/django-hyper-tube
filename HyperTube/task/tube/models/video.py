from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()

    @staticmethod
    def find_all():
        return Video.objects.all()
