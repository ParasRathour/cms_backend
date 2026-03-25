from django.contrib import admin
from .models import (
    ContactSubmission,
    DemoRequestSubmission,
    AdmissionFormSubmission,
    InternshipApplicationSubmission,
)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "submitted_at", "read")
    list_filter = ("read", "submitted_at")
    search_fields = ("name", "email", "subject")
    readonly_fields = ("submitted_at", "ip_address")


@admin.register(DemoRequestSubmission)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = (
        "organization_name",
        "contact_person",
        "email",
        "status",
        "submitted_at",
        "read",
    )
    list_filter = ("status", "read")
    search_fields = ("organization_name", "contact_person", "email")
    readonly_fields = ("submitted_at", "ip_address")


@admin.register(AdmissionFormSubmission)
class AdmissionFormAdmin(admin.ModelAdmin):
    list_display = ("submission_id", "status", "submitted_at")
    list_filter = ("status",)
    search_fields = ("submission_id",)
    readonly_fields = ("submitted_at", "updated_at", "ip_address")


@admin.register(InternshipApplicationSubmission)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "job_position", "status", "submitted_at")
    list_filter = ("status", "job_position")
    search_fields = ("full_name", "email", "college")
    readonly_fields = ("submitted_at", "ip_address")
