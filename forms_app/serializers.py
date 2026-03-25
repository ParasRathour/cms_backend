from rest_framework import serializers
from .models import (
    ContactSubmission,
    DemoRequestSubmission,
    AdmissionFormSubmission,
    InternshipApplicationSubmission,
)


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = "__all__"
        read_only_fields = ("submitted_at", "ip_address", "read")


class DemoRequestSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoRequestSubmission
        fields = "__all__"
        read_only_fields = ("submitted_at", "ip_address", "read")


class AdmissionFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionFormSubmission
        fields = "__all__"
        read_only_fields = ("submitted_at", "updated_at", "ip_address")


class InternshipApplicationSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipApplicationSubmission
        fields = "__all__"
        read_only_fields = ("submitted_at", "ip_address")
