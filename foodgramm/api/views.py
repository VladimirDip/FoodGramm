from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Favorites
from api.serializers import IngredientSerializer, FavoriteSerializer
from recipes.models import Ingredient
from .logic import validate_author


class CreateDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^title',)


class FavoriteViewSet(CreateDestroyViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'recipe'
    queryset = Favorites.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)










