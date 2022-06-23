from django.contrib import admin

from .models import Character
from .models import OfficeUpgrade
from .models import UserProfile
from .models import UserProfileOfficeUpgrade


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "character_name",
        "character_gender",
        "character_faction",
        "character_race",
        "character_class",
    )


admin.site.register(Character, CharacterAdmin)
admin.site.register(OfficeUpgrade)
admin.site.register(UserProfile)
admin.site.register(UserProfileOfficeUpgrade)
