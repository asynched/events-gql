import graphene
from graphene_django import DjangoObjectType

from events.models import Speaker, SpeakerSocialMedia
from events.graphql.speaker_social_media.schema import SpeakerSocialMediaType


class SpeakerType(DjangoObjectType):
    social_media = graphene.Field(SpeakerSocialMediaType)

    def resolve_social_media(self, info):
        try:
            return SpeakerSocialMedia.objects.get(speaker=self.id)
        except SpeakerSocialMedia.DoesNotExist:
            return None

    class Meta:
        model = Speaker
        exclude = (
            "speakersocialmedia",
            "keynotespeaker_set",
        )


class SpeakerQueries(graphene.ObjectType):
    all_speakers = graphene.List(SpeakerType)
    speaker = graphene.Field(SpeakerType, id=graphene.UUID(required=True))

    def resolve_all_speakers(root, info):
        return Speaker.objects.all()

    def resolve_speaker(root, info, id: str):
        return Speaker.objects.get(id=id)
