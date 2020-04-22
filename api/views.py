from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import ApiKeyPermission
from api.serializers import ApplicationSerializer
from core.models import Application


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all().order_by('is_active', 'name', '-created')

    @action(methods=['post'], detail=True)
    def refresh_apikey(self, request, *args, **kwargs):
        app = self.get_object()
        try:
            app.create_apikey()
            return Response({"API_KEY": app.api_key})
        except Exception as ex:
            return Response({"error": ex})


class TestView(APIView):
    http_method_names = ('get',)
    permission_classes = (ApiKeyPermission, )

    def get(self, request, format=None):
        return Response({'Test view'})
