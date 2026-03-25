from rest_framework import serializers
from .models import Instructor, Course, CourseModule, CourseFAQ


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = "__all__"


class CourseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModule
        fields = "__all__"


class CourseFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFAQ
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    modules = CourseModuleSerializer(
        source="coursemodule_set", many=True, read_only=True
    )
    faqs = CourseFAQSerializer(source="coursefaq_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
