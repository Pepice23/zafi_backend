from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .bad_words import check_text
from .models import Character
from .serializers import CharacterSerializer


class ListCharacter(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class NameCheck(APIView):
    def get(self, request, name: str):
        queryset = User.objects.all()
        if name is not None:
            queryset = queryset.filter(username=name)
            if len(queryset) > 0:
                return HttpResponseBadRequest(
                    f"There is already a user named: {name} in the database"
                )
            else:
                return Response(name)
        else:
            return HttpResponseBadRequest(name)


class NewCharacter(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
