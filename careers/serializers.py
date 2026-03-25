from rest_framework import serializers
from .models import CareerPage, JobPosition


class CareerPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPage
        fields = "__all__"


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = "__all__"
