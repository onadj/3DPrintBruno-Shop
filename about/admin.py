from django.contrib import admin
from .models import About
from django.utils.safestring import mark_safe
from django.utils.html import format_html


from django.utils.html import format_html

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'video_url')

    def get_image(self, obj):
        if obj.images.exists():
            first_image = obj.images.first()
            return format_html('<img src="{}" width="50" height="50" />', first_image.image.url)
        return 'No Image'

    get_image.short_description = 'Image'

