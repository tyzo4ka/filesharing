from django.contrib import admin
from webapp.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'file', 'author', 'caption', 'access', 'created_at']
    list_filter = ['author', 'created_at']
    exclude = []
    readonly_fields = ['created_at']

admin.site.register(File, FileAdmin)