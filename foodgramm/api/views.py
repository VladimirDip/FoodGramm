from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters

from api.serializers import IngredientSerializer
from recipes.models import Ingredient


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^title',)