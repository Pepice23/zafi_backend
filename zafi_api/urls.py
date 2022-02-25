from django.urls import path
from .views import ListCharacter, DetailCharacter

urlpatterns = [
    path("<str:pk>/", DetailCharacter.as_view(), name="character_detail"),
    path("", ListCharacter.as_view(), name="character_list"),
]
