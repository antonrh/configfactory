from django.urls import path

from configfactory.api.views import IndexAPIView

app_name = "api"

urlpatterns = [path("", IndexAPIView.as_view())]
