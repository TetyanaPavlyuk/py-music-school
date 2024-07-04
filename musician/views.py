from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
