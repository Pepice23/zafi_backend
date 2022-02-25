# Generated by Django 4.0.2 on 2022-02-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_name', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Character name:')),
                ('character_gender', models.CharField(max_length=6, verbose_name='Character gender:')),
                ('character_faction', models.CharField(max_length=8, verbose_name='Faction')),
                ('character_race', models.CharField(max_length=32, verbose_name='Race')),
                ('character_class', models.CharField(max_length=32, verbose_name='Player Class')),
            ],
        ),
    ]
