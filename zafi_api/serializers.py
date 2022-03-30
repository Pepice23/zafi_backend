from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "character_name",
            "character_gender",
            "character_faction",
            "character_race",
            "character_class",
            "race_uid",
        )
