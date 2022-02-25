from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer


class ListCharacter(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
