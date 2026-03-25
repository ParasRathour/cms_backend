from django.urls import path
from .views import CourseListView, CourseDetailView, CourseSearchView

urlpatterns = [
    path("", CourseListView.as_view()),
    path("search/", CourseSearchView.as_view()),
    path("<slug:slug>/", CourseDetailView.as_view()),
]
