from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "email", "phone"]
    fieldsets = UserAdmin.fieldsets + (
        ("Addiational Information", {"fields": ("bio", "date_of_birth", "photo", "job", "phone")}),
    )
