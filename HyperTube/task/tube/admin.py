from django.contrib import admin

from .models.tag import Tag
from .models.video import Video
from .models.video_tag import VideoTag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    fields = ("id", "name")
    readonly_fields = ("id",)


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "file", "id")
    fields = ("id", "title", "file")
    readonly_fields = ("id", "file")


class VideoTagAdmin(admin.ModelAdmin):
    list_display = ("tag", "video")
    fields = ("tag", "video")
    readonly_fields = ("tag", "video")


admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoTag, VideoTagAdmin)
