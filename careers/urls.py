from django.urls import path
from .views import CareerPageView, JobPositionListView, JobPositionDetailView

urlpatterns = [
    path("page/", CareerPageView.as_view()),
    path("positions/", JobPositionListView.as_view()),
    path("positions/<int:pk>/", JobPositionDetailView.as_view()),
]
