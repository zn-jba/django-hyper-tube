from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name
