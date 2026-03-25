from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import GalleryImage, ProjectCaseStudy, Partner
from .serializers import (
    GalleryImageSerializer,
    ProjectCaseStudySerializer,
    PartnerSerializer,
)


class GalleryImageListView(generics.ListAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class ProjectCaseStudyListView(generics.ListAPIView):
    queryset = ProjectCaseStudy.objects.all()
    serializer_class = ProjectCaseStudySerializer


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
