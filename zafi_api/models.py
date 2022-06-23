from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    character_name = models.CharField(
        max_length=32, primary_key=True, unique=True, verbose_name="Character name:"
    )
    character_gender = models.CharField(max_length=6, verbose_name="Character gender:")
    character_faction = models.CharField(max_length=8, verbose_name="Faction:")
    character_race = models.CharField(max_length=32, verbose_name="Race:")
    character_class = models.CharField(max_length=32, verbose_name="Player Class:")
    race_uid = models.CharField(max_length=32, verbose_name="Race UID:", default="")
    character_xp = models.IntegerField(verbose_name="XP:", default=0)
    required_xp = models.IntegerField(verbose_name="Required XP:", default=400)
    level = models.IntegerField(verbose_name="Level:", default=1)
    item_level = models.IntegerField(verbose_name="Item Level:", default=0)
    character_money = models.IntegerField(verbose_name="Money:", default=0)

    def __str__(self):
        return self.character_name


class OfficeUpgrade(models.Model):
    add_money_per_sec = models.IntegerField(
        verbose_name="Add money per second:", default=0
    )
    do_work_per_sec = models.IntegerField(verbose_name="Do work per second:", default=0)
    add_money_per_click = models.IntegerField(
        verbose_name="Add money per click:", default=0
    )
    do_work_per_click = models.IntegerField(
        verbose_name="Do work per click:", default=0
    )
    office_upgrade_timer = models.IntegerField(verbose_name="Timer:", default=0)
    office_upgrade_name = models.CharField(max_length=32, verbose_name="Upgrade name:")

    def __str__(self):
        return self.office_upgrade_name
