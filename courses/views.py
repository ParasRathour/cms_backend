from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer


# List + filter
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "level", "featured"]


# Detail (slug)
class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "slug"


# Search
class CourseSearchView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]
