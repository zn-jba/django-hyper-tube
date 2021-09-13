from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.title

    @staticmethod
    def find_all():
        return Video.objects.all()
