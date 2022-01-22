from graphene_django import DjangoObjectType

from events.models import KeynoteSpeaker


class KeynoteSpeakerType(DjangoObjectType):
    class Meta:
        model = KeynoteSpeaker
        fields = "__all__"
