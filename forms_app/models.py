from django.db import models
from careers.models import JobPosition


# Contact form
class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    submitted_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)


# Demo request form
class DemoRequestSubmission(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("scheduled", "Scheduled"),
        ("closed", "Closed"),
    ]
    organization_name = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cohort_size = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    submitted_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    notes = models.TextField(blank=True, null=True)


# Admission form submission
class AdmissionFormSubmission(models.Model):
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("verified", "Verified"),
        ("admitted", "Admitted"),
        ("rejected", "Rejected"),
    ]
    submission_id = models.CharField(max_length=20, unique=True)
    personal = models.JSONField()
    contact = models.JSONField()
    address = models.JSONField()
    family = models.JSONField()
    education = models.JSONField()
    preferences = models.JSONField()
    additional = models.JSONField(blank=True, null=True)
    documents = models.FileField(upload_to="admissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="submitted"
    )
    notes = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")


# Internship application
class InternshipApplicationSubmission(models.Model):
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected"),
    ]

    job_position = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=300)
    degree = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=4)
    cover_letter = models.TextField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to="internships/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="submitted"
    )
    notes = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
