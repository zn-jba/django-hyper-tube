from django.contrib import admin

from .models.tag import Tag
from .models.video import Video
from .models.video_tag import VideoTag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "id")
    fields = ("id", "title")
    readonly_fields = ("id",)


class VideoTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoTag, VideoTagAdmin)
