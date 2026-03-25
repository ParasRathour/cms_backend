from django.db import models


# Gallery images
class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/%Y/%m/")
    alt = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


# Project case studies
class ProjectCaseStudy(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to="projects/")
    outcomes = models.JSONField(default=list)
    location = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Partner logos
class Partner(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to="partners/")
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
