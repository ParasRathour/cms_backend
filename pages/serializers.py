from rest_framework import serializers
from .models import SiteMeta, HomePage, AboutPage, ServicesPage


class SiteMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMeta
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = "__all__"


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = "__all__"


class ServicesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPage
        fields = "__all__"
