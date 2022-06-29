from django.urls import path
from .views import (
    ListCharacter,
    DetailCharacter,
    CharacterNameCheck,
    NewCharacter,
    UserNameCheck,
)

urlpatterns = [
    path("character/new/", NewCharacter.as_view(), name="newcharacter"),
    path("namecheck/<str:name>", CharacterNameCheck.as_view(), name="name_check"),
    path("usernamecheck/<str:name>", UserNameCheck.as_view(), name="username_check"),
    path("<str:pk>/", DetailCharacter.as_view(), name="character_detail"),
    path("", ListCharacter.as_view(), name="character_list"),
]
