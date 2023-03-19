from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'stars', 'review')
    search_fields = ['first_name', 'created', 'stars']
    list_filter = ['created', 'stars']
    summernote_fields = ('review', 'reply',)
