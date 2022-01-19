import graphene
from events.graphql.speaker.schema import SpeakerQueries


class Query(
    SpeakerQueries,
):
    pass


schema = graphene.Schema(query=Query)
