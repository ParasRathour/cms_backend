from django.db import models


class SiteMeta(models.Model):
    site_name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500)
    description = models.TextField()
    logo = models.ImageField(upload_to="site_meta/")
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    whatsapp = models.CharField(max_length=20)
    social = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Site Meta"


# HomePage content
class HomePage(models.Model):
    hero_title = models.CharField(max_length=300)
    hero_subtitle = models.CharField(max_length=300)
    hero_description = models.TextField()
    hero_cta_primary = models.JSONField(default=dict)
    hero_cta_secondary = models.JSONField(default=dict)
    pillars = models.JSONField(default=list)
    stats = models.JSONField(default=list)
    featured_projects = models.JSONField(default=list)
    partners = models.JSONField(default=list)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Home Page"


# AboutPage
class AboutPage(models.Model):
    company_name = models.CharField(max_length=200)
    founded_year = models.IntegerField()
    company_overview = models.TextField()
    company_mission = models.TextField()
    company_vision = models.TextField()
    founder_name = models.CharField(max_length=200)
    founder_title = models.CharField(max_length=200)
    founder_bio = models.TextField()
    founder_image = models.ImageField(upload_to="founders/")
    timeline = models.JSONField(default=list)
    business_profile_pdf = models.FileField(
        upload_to="business_profile/", blank=True, null=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "About Page"


# ServicesPage
class ServicesPage(models.Model):
    services = models.JSONField(default=list)
    trainings = models.JSONField(default=list)
    drt_open_school = models.JSONField(default=list)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Services Page"
