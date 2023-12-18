from django.contrib import admin
from .models import Post, Ticket, Comment


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

    search_fields = ["title", "description", "author__first_name", "author__last_name"]
    raw_id_fields = ["author"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "phone_number", "email"]
    list_editable = ["subject"]
    list_display_links = ["title", "phone_number", "email"]
    list_filter = ["subject"]

    search_fields = ["title", "message"]


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "create_date", "active"]
    list_editable = ["active"]
    list_display_links = ["author", "create_date"]
    list_filter = ["active", "create_date", "author"]

    ordering = ["create_date"]

    date_hierarchy = "create_date"

    search_fields = ["text", "author__first_name", "author__last_name"]
    raw_id_fields = ["author", "post"]
