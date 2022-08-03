from django import template
from django.contrib.auth import get_user_model


register = template.Library()
User = get_user_model()


@register.filter
def get_full_name_or_username(user):
    return user.get_full_name() or user.username


@register.filter
def tags_to_url_params(tags):
    return '&' + '&'.join([f'tag={tag}' for tag in tags])

