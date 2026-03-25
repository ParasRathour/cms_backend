from django.contrib import admin

from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_admin", "is_staff", "is_active")
    list_filter = ("is_admin", "is_staff", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("created_at", "updated_at")
