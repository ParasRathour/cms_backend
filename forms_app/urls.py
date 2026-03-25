from django.urls import path
from .views import (
    ContactSubmissionCreateView,
    DemoRequestCreateView,
    AdmissionFormCreateView,
    InternshipApplicationCreateView,
)

urlpatterns = [
    path("contact/", ContactSubmissionCreateView.as_view()),
    path("demo-request/", DemoRequestCreateView.as_view()),
    path("admission/", AdmissionFormCreateView.as_view()),
    path(
        "internship-apply/<int:job_position_id>/",
        InternshipApplicationCreateView.as_view(),
    ),
]
