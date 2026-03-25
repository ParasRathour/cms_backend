from django.urls import path
from .views import GalleryImageListView, ProjectCaseStudyListView, PartnerListView

urlpatterns = [
    path("", GalleryImageListView.as_view()),
    path("projects/", ProjectCaseStudyListView.as_view()),
    path("partners/", PartnerListView.as_view()),
]
