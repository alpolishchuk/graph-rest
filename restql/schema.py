import graphene

import restql.graph.schema


class Query(restql.graph.schema.Query, graphene.ObjectType):
    pass


class Mutation(restql.graph.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


