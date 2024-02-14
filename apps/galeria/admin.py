from django.contrib import admin
from apps.galeria.models import Photograph

class PhotographAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "category", "published", "created", "modified")
    list_display_links = ("id", "name")
    empty_value_display = '-empty-'
    fields = (('name', 'legend'), ("category", "published"), "file", "description", "created", "modified", "user")
    readonly_fields = ("created", "modified")
    search_fields = ("name",)
    list_filter = ("category", "user",)
    list_editable = ("published",)
    list_per_page = 10

admin.site.register(Photograph, PhotographAdmin)
