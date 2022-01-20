import graphene

from events.graphql.stage.schema import StageQueries
from events.graphql.keynote.schema import KeynoteQueries
from events.graphql.speaker.schema import SpeakerQueries


class Query(
    SpeakerQueries,
    StageQueries,
    KeynoteQueries,
):
    pass


schema = graphene.Schema(query=Query)
