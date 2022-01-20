import graphene
from graphene_django import DjangoObjectType
from events.graphql.keynote.schema import KeynoteType

from events.models import Keynote, Stage


class StageType(DjangoObjectType):
    keynotes = graphene.List(KeynoteType)

    def resolve_keynotes(self, info):
        return Keynote.objects.filter(stage=self.id)

    class Meta:
        model = Stage
        exclude = ('keynote_set',)

class StageQueries(graphene.ObjectType):
    all_stages = graphene.List(StageType)
    stage = graphene.Field(StageType, id=graphene.UUID(required=True))

    def resolve_all_stages(root, info):
        return Stage.objects.all()
    
    def resolve_stage(root, info, id):
        try:
            Stage.objects.get(id=id)
        except Stage.DoesNotExist:
            return None
