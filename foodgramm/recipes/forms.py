from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import Recipe, Tag
from django import forms


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'tags', 'cooking_time', 'text', 'image')
        widgets = {'tags': forms.CheckboxSelectMultiple()}
        labels = {
            'ingredients': _('Ингридиенты'),
        }





