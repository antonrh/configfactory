from django.urls import include, path

from configfactory.views import IndexView

urlpatterns = [
    path("", IndexView.as_view()),
    path("api/", include("configfactory.api.urls")),
]
