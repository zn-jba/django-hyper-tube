from django.db import models

from .tag import Tag
from .video import Video


class VideoTag(models.Model):
    tag = models.ForeignKey(Tag, related_name="tag", on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="video", on_delete=models.CASCADE)
