from django.db import models


# Instructor profiles
class Instructor(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="instructors/")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    expertise = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Courses
class Course(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    mode = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500)
    short_description = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    price = models.JSONField(default=dict)
    highlights = models.JSONField(default=list)
    learning_outcomes = models.JSONField(default=list)
    requirements = models.JSONField(default=list, blank=True, null=True)
    career_opportunities = models.JSONField(default=list, blank=True, null=True)
    students_enrolled = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    certification = models.CharField(max_length=300, blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Modules inside course
class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)
    topics = models.JSONField(default=list)
    description = models.TextField(blank=True, null=True)
    learning_outcomes = models.JSONField(default=list, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# FAQs for course
class CourseFAQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
