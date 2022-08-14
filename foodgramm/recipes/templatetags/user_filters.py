from django import template
from django.contrib.auth import get_user_model
from api.models import Favorites

register = template.Library()
User = get_user_model()


@register.filter
def get_full_name_or_username(user):
    return user.get_full_name() or user.username


@register.filter
def tags_to_url_params(tags):
    return '&' + '&'.join([f'tag={tag}' for tag in tags])


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def is_favored_by(recipe, user):
    return Favorites.objects.filter(recipe=recipe, user=user).exists()

