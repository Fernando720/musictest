from rest_framework import viewsets
from .models import Songs
from .serializers import SongsSerializer

class ListSongsView(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
