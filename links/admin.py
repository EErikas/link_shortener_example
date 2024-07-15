from django.contrib import admin
from .models import Link, Click


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('shortened_link', 'original_url')

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('source_ip', 'link', 'time')