from django.contrib import admin
from .models import Post


# Title
# admin.sites.AdminSite.site_title = "پنل" # Django site administration
# Index title
# admin.sites.AdminSite.index_title = "پنل مدیریت" # Site administration
# Header
# admin.sites.AdminSite.site_header = "پنل مدیریت جنگو" # Django administration


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
