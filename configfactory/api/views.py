from rest_framework.response import Response

from configfactory.core.api.views import APIView


class IndexAPIView(APIView):
    def get(self, request):
        return Response("Hello, ConfigFactory API !")
