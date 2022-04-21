from flask_graphql import GraphQLView
from .gql import Query, Mutation
from graphene import Schema
from .appinit import app

app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=Schema(
                query=Query,
                mutation=Mutation,
            ),
            graphiql=True,
        ),
    )