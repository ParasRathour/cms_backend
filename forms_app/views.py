from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import (
    ContactSubmission,
    DemoRequestSubmission,
    AdmissionFormSubmission,
    InternshipApplicationSubmission,
)
from .serializers import (
    ContactSubmissionSerializer,
    DemoRequestSubmissionSerializer,
    AdmissionFormSubmissionSerializer,
    InternshipApplicationSubmissionSerializer,
)


# Contact
class ContactSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def perform_create(self, serializer):
        ip = self.request.META.get("REMOTE_ADDR")
        serializer.save(ip_address=ip)


# Demo
class DemoRequestCreateView(generics.CreateAPIView):
    queryset = DemoRequestSubmission.objects.all()
    serializer_class = DemoRequestSubmissionSerializer

    def perform_create(self, serializer):
        ip = self.request.META.get("REMOTE_ADDR")
        serializer.save(ip_address=ip)


# Admission (file upload)
class AdmissionFormCreateView(generics.CreateAPIView):
    queryset = AdmissionFormSubmission.objects.all()
    serializer_class = AdmissionFormSubmissionSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        ip = self.request.META.get("REMOTE_ADDR")
        serializer.save(ip_address=ip)


# Internship (with position_id)
class InternshipApplicationCreateView(generics.CreateAPIView):
    queryset = InternshipApplicationSubmission.objects.all()
    serializer_class = InternshipApplicationSubmissionSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        ip = self.request.META.get("REMOTE_ADDR")
        job_position_id = self.kwargs.get("job_position_id")
        serializer.save(ip_address=ip, job_position_id=job_position_id)
