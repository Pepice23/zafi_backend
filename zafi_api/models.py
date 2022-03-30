from django.db import models


class Character(models.Model):
    character_name = models.CharField(
        max_length=32, primary_key=True, unique=True, verbose_name="Character name:"
    )
    character_gender = models.CharField(max_length=6, verbose_name="Character gender:")
    character_faction = models.CharField(max_length=8, verbose_name="Faction")
    character_race = models.CharField(max_length=32, verbose_name="Race")
    character_class = models.CharField(max_length=32, verbose_name="Player Class")
    race_uid = models.CharField(max_length=32, verbose_name="Race UID", default="")

    def __str__(self):
        return self.character_name
