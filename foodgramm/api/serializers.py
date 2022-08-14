from rest_framework import serializers

from recipes.models import Ingredient
from .models import Favorites
# from .logic import validate_author


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('title', 'dimension')


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorites
        fields = ('recipe', 'user')

    # def validate_author(self, data):
    #     print(f'выполняется {data.get("author")} и {data.get("user")}')
    #     if data.get('author') == data.get('user'):
    #         raise serializers.ValidationError('Нельзя добавить в избраное свой рецепт')
    #     return data
