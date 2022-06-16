# Generated by Django 4.0.2 on 2022-06-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zafi_api', '0002_character_race_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_money',
            field=models.IntegerField(default=0, verbose_name='Money:'),
        ),
        migrations.AddField(
            model_name='character',
            name='character_xp',
            field=models.IntegerField(default=0, verbose_name='XP:'),
        ),
        migrations.AddField(
            model_name='character',
            name='item_level',
            field=models.IntegerField(default=0, verbose_name='Item Level:'),
        ),
        migrations.AddField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Level:'),
        ),
        migrations.AddField(
            model_name='character',
            name='required_xp',
            field=models.IntegerField(default=400, verbose_name='Required XP:'),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.CharField(max_length=32, verbose_name='Player Class:'),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_faction',
            field=models.CharField(max_length=8, verbose_name='Faction:'),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_race',
            field=models.CharField(max_length=32, verbose_name='Race:'),
        ),
        migrations.AlterField(
            model_name='character',
            name='race_uid',
            field=models.CharField(default='', max_length=32, verbose_name='Race UID:'),
        ),
    ]