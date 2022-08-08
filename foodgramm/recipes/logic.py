from decimal import Decimal

from django.db import transaction
from django.shortcuts import get_object_or_404

from recipes.models import Ingredient, RecipeIngredient


def get_request_tags(request):
    return request.GET.getlist('tag', ('breakfast', 'lunch', 'dinner'))


def get_ingredients(requests):
    ingredients = {}
    post = requests.POST
    print(f'this is post {post}')
    for key, name in post.items():
        if key.startswith('nameIngredient'):
            print(f'key = {key}, name = {name}')
            num = key.partition('_')[-1]
            ingredients[name] = post[f'valueIngredient_{num}']

    return ingredients


def save_recipe(request, form):
    with transaction.atomic():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()

        objs = []
        ingredients = get_ingredients(request)
        print(f'this is ingredients from save_recipe {ingredients}')

        for name, quantity in ingredients.items():
            ingredient = get_object_or_404(Ingredient, title=name)
            objs.append(
                RecipeIngredient(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=Decimal(quantity.replace(',', '.'))
                )
            )
        print(objs)
        RecipeIngredient.objects.bulk_create(objs)
        form.save_m2m()
        return recipe


def edit_recipe(request, form, instance):
    with transaction.atomic():
        RecipeIngredient.objects.filter(recipe=instance).delete()
        return save_recipe(request, form)