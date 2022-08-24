from rest_framework import serializers

from recipes.models import Ingredient
from .models import Favorites, Subscriptions
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


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscriptions
        fields = ('user', 'author')

    def validate(self, data):
        print(f'выполняется {data["author"]} и {data["user"]}')
        if data['author'] == data['user']:
            raise serializers.ValidationError('Нельзя добавить подписаться на самого себя')
        return data
