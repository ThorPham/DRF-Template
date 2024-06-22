from rest_framework import mixins
from rest_framework import generics
from app.models import Supporter
from app.serializers import SupporterSerializer

class SupporterAV(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)