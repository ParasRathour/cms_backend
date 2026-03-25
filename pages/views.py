from rest_framework import generics
from .models import SiteMeta, HomePage, AboutPage, ServicesPage
from .serializers import (
    SiteMetaSerializer,
    HomePageSerializer,
    AboutPageSerializer,
    ServicesPageSerializer,
)


class SiteMetaView(generics.RetrieveAPIView):
    queryset = SiteMeta.objects.all()
    serializer_class = SiteMetaSerializer

    def get_object(self):
        return self.queryset.first()


class HomePageView(generics.RetrieveAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

    def get_object(self):
        return self.queryset.first()


class AboutPageView(generics.RetrieveAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer

    def get_object(self):
        return self.queryset.first()


class ServicesPageView(generics.RetrieveAPIView):
    queryset = ServicesPage.objects.all()
    serializer_class = ServicesPageSerializer

    def get_object(self):
        return self.queryset.first()
