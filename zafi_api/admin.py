from django.contrib import admin

from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "character_name",
        "character_gender",
        "character_faction",
        "character_race",
        "character_class",
    )


admin.site.register(Character, CharacterAdmin)
