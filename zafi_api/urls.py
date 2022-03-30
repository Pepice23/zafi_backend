from django.urls import path
from .views import ListCharacter, DetailCharacter, NameCheck, NewCharacter

urlpatterns = [
    path("character/new/", NewCharacter.as_view(), name="newcharacter"),
    path("namecheck/<str:name>", NameCheck.as_view(), name="name_check"),
    path("<str:pk>/", DetailCharacter.as_view(), name="character_detail"),
    path("", ListCharacter.as_view(), name="character_list"),
]
