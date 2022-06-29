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


class UserNameCheck(APIView):
    def get(self, request, name: str):
        queryset = User.objects.all()
        if name is not None:
            check_name = check_text(name.lower())
            if check_name == name:
                queryset = queryset.filter(username=name.lower())
                if len(queryset) > 0:
                    return HttpResponseBadRequest(
                        f"There is already a username: {name} in the database"
                    )
                else:
                    return Response(name)
            else:
                return HttpResponseBadRequest(check_name)


class CharacterNameCheck(APIView):
    def get(self, request, name: str):
        success_name = {"name": name.capitalize()}
        queryset = Character.objects.all()
        if name is not None:
            check_name = check_text(name)
            if check_name == name:
                queryset = queryset.filter(character_name=name.capitalize())
                if len(queryset) > 0:
                    return HttpResponseBadRequest(
                        f"There is already a character named: {name} in the database"
                    )
                else:
                    return Response(success_name)
            else:
                return HttpResponseBadRequest(check_name)


class NewCharacter(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
