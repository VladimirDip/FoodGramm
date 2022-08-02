from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe, Tag

from .logic import get_request_tags


class IndexListView(ListView):
    model = Recipe
    template_name = 'indexNotAuth.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        self.recipes = Recipe.objects.filter(tags__title__in=get_request_tags(
            request=self.request)).select_related(
            'author').prefetch_related(
            'tags').distinct()
        return self.recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'singlePageNotAuth.html'
    context_object_name = 'recipes'