from django.db import models


class Video(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def find_all():
        return Video.objects.all()
