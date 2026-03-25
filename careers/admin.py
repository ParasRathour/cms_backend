from django.contrib import admin
from .models import CareerPage, JobPosition


@admin.register(CareerPage)
class CareerPageAdmin(admin.ModelAdmin):
    readonly_fields = ("updated_at",)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "job_type", "status", "featured")
    list_filter = ("job_type", "status", "featured")
    search_fields = ("title", "department", "location")
    readonly_fields = ("created_at", "updated_at")
