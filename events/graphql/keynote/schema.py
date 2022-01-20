import graphene
from graphene_django import DjangoObjectType

from events.models import Keynote

class KeynoteType(DjangoObjectType):
    class Meta:
        model = Keynote
        exclude = ('stage',)

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
