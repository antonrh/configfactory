from django.urls import path

from configfactory.views import index

urlpatterns = [path("", index)]
