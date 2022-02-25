from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .bad_words import check_text
from .models import Character
from .serializers import CharacterSerializer


class ListCharacter(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class NameCheck(APIView):
    def get(self, request, name: str):
        queryset = Character.objects.all()
        if name is not None:
            check_name = check_text(name)
            if check_name == name:
                queryset = queryset.filter(character_name=name.capitalize())
                if len(queryset) > 0:
                    return Response(
                        f"There is already a character named: {name} in the database"
                    )
            else:
                return Response(check_name)
