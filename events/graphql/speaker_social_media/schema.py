import graphene
from graphene_django import DjangoObjectType
from events.models import SpeakerSocialMedia


class SpeakerSocialMediaType(DjangoObjectType):
    class Meta:
        model = SpeakerSocialMedia
        exclude = ("speaker",)
