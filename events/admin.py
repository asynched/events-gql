from django.contrib import admin
from events.models import (
    Stage,
    Speaker,
    Keynote,
    KeynoteSpeaker,
    SpeakerSocialMedia,
)


admin.site.register(Stage)
admin.site.register(Speaker)
admin.site.register(Keynote)
admin.site.register(KeynoteSpeaker)
admin.site.register(SpeakerSocialMedia)
