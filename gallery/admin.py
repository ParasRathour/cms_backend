from django.contrib import admin
from .models import GalleryImage, ProjectCaseStudy, Partner


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("alt", "category", "year", "order", "created_at")
    list_filter = ("category", "year")
    readonly_fields = ("created_at",)


@admin.register(ProjectCaseStudy)
class ProjectCaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "created_at")
    readonly_fields = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "order", "created_at")
    readonly_fields = ("created_at",)
