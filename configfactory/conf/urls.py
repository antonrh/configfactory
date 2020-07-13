from django.urls import include, path

from configfactory.views import index

urlpatterns = [path("", index), path("api/", include("configfactory.api.urls"))]
