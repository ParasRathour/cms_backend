from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CareerPage, JobPosition
from .serializers import CareerPageSerializer, JobPositionSerializer


class CareerPageView(generics.RetrieveAPIView):
    queryset = CareerPage.objects.all()
    serializer_class = CareerPageSerializer

    def get_object(self):
        return self.queryset.first()


class JobPositionListView(generics.ListAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["job_type", "department", "status", "featured"]
    search_fields = ["title", "department", "location"]


class JobPositionDetailView(generics.RetrieveAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
