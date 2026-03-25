from django.urls import path
from .views import SiteMetaView, HomePageView, AboutPageView, ServicesPageView

urlpatterns = [
    path(
        "",
    ),
    path("site/meta/", SiteMetaView.as_view()),
    path("home/", HomePageView.as_view()),
    path("about/", AboutPageView.as_view()),
    path("services/", ServicesPageView.as_view()),
]
