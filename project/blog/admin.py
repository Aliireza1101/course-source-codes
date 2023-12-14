from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publish_date", "status"]
    list_editable = ["status"]
    list_display_links = ["title", "author", "publish_date"]
    list_filter = ["status", "publish_date", "author"]

    ordering = ["create_date"]

    prepopulated_fields = {"slug": ["title"]}
    date_hierarchy = "create_date"

    search_fields = ["title", "description", "author"]
    raw_id_fields = ["author"]
