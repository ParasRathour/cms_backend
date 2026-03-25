from django.db import models


# Career page singleton
class CareerPage(models.Model):
    page_title = models.CharField(max_length=300)
    page_subtitle = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    culture = models.JSONField(default=list)
    benefits = models.JSONField(default=list)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce singleton
        super().save(*args, **kwargs)

    def __str__(self):
        return "Career Page"


# Job/internship positions


class JobPosition(models.Model):
    JOB_TYPES = [
        ("full-time", "Full-time"),
        ("part-time", "Part-time"),
        ("internship", "Internship"),
    ]
    STATUS_CHOICES = [
        ("open", "Open"),
        ("closed", "Closed"),
    ]

    title = models.CharField(max_length=300)
    department = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    experience = models.CharField(max_length=200)
    description = models.TextField()
    responsibilities = models.JSONField(default=list)
    qualifications = models.JSONField(default=list)
    skills = models.JSONField(default=list)
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
