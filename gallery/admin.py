from django.contrib import admin
from .models import Image
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Image)
class ImageAdmin(SummernoteModelAdmin):

    list_display = ('title', 'type', 'published')
    search_fields = ['title', 'type']
    list_filter = ['type', 'published']
    actions = ['publish_selected_images']

    def publish_selected_images(self, request, queryset):
        queryset.update(published=True)
