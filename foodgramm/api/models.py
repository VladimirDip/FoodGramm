from django.db import models
from django.contrib.auth import get_user_model

from recipes.models import Recipe

User = get_user_model()


class Subscriptions(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='Подпислся на'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_subscription'
            )
        ]
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class Favorites(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorite_by',
        verbose_name='Рецепт в избраном'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorite'
            )
        ]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ['user']

    def __str__(self):
        return f'{self.user} добавил рецепт "{self.recipe}" в избраное'


class Purchases(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='purchases',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт в покупках'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_purchase'
            )
        ]
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'