import graphene
import meetup.schema

class Query(meetup.schema.Query, graphene.ObjectType):
    """
    This class imports from other queries as we add more apps
    """
    pass

schema = graphene.Schema(query=Query)