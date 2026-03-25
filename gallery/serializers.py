from rest_framework import serializers
from .models import GalleryImage, ProjectCaseStudy, Partner


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"


class ProjectCaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCaseStudy
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
