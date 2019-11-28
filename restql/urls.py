from django.urls import path, include
from graphene_django.views import GraphQLView

from restql.schema import schema

urlpatterns = [
    path(r'rest/', include('restql.rest.urls')),
    path(r'graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

