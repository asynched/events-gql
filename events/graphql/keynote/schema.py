import graphene
from graphene_django import DjangoObjectType

from events.models import Keynote
from events.graphql.keynote_speaker.schema import KeynoteSpeakerType
from events.models import KeynoteSpeaker


class KeynoteType(DjangoObjectType):
    keynote_speakers = graphene.List(KeynoteSpeakerType)

    def resolve_keynote_speakers(self, info):
        return KeynoteSpeaker.objects.filter(keynote=self.id)

    class Meta:
        model = Keynote
        exclude = ("stage",)


class KeynoteQueries(graphene.ObjectType):
    all_keynotes = graphene.List(KeynoteType)
    keynote = graphene.Field(KeynoteType)

    def resolve_all_keynotes(root, info):
        return Keynote.objects.all()

    def resolve_keynote(root, info, id):
        try:
            Keynote.objects.get(id=id)
        except Keynote.DoesNotExist:
            return None
