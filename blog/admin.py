from django.contrib import admin
from .models import Post, Ticket, Comment, Image, Account


# Title
# admin.sites.AdminSite.site_title = "پنل" # Django site administration
# Index title
# admin.sites.AdminSite.index_title = "پنل مدیریت" # Site administration
# Header
# admin.sites.AdminSite.site_header = "پنل مدیریت جنگو" # Django administration


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


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

    inlines = (
        ImageInline,
        CommentInline,
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "subject", "active"]
    list_editable = ["subject", "active"]
    list_display_links = [
        "title",
    ]
    list_filter = ["subject"]

    search_fields = ["title", "message"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "create_date", "is_active"]
    list_editable = ["is_active"]
    list_display_links = ["author", "create_date"]
    list_filter = ["is_active", "create_date", "author"]

    ordering = ["create_date"]

    date_hierarchy = "create_date"

    search_fields = ["text", "author__first_name", "author__last_name"]
    raw_id_fields = ["author", "post"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["post", "title", "create_date"]
    list_display_links = list_display
    list_filter = ["create_date"]

    ordering = ["create_date"]

    date_hierarchy = "create_date"

    search_fields = ["title", "description", "post__title"]
    raw_id_fields = ["post"]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth"]
    list_display_links = list_display
    list_filter = ["date_of_birth"]

    ordering = ["date_of_birth"]
    date_hierarchy = "date_of_birth"

    search_fields = ["user__username", "user__first_name", "user__last_name"]
    raw_id_fields = ["user"]
