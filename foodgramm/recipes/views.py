from django.shortcuts import redirect, get_object_or_404, render
from django.db.models.signals import m2m_changed
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from api.models import Favorites
from .logic import get_request_tags, save_recipe, edit_recipe
from .models import Recipe, Tag
from .forms import RecipeForm


class IndexListView(ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'
    paginate_by = 2

    def get_queryset(self):
        self.recipes = Recipe.objects.filter(tags__title__in=get_request_tags(
            request=self.request)).select_related(
            'author').prefetch_related(
            'tags').order_by('-pk').distinct('pk')

        return self.recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        # print(context)
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'singlePageNotAuth.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


class RecipeCreateView(CreateView):
    template_name = 'formRecipe.html'
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        recipe_saved = save_recipe(self.request, form)
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('recipe_view_slug', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Создать рецепт'
        return context


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'formRecipe.html'
    form_class = RecipeForm

    def form_valid(self, form):
        recipe_saved = edit_recipe(self.request, form, instance=form.instance)
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('recipe_view_slug', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Обновить рецепт'
        return context


class FavoritesListView(ListView):
    model = Favorites
    context_object_name = 'favorites'
    paginate_by = 3
    template_name = 'favorite.html'

    def get_queryset(self):
        self.favorites = Favorites.objects.filter(
            user_id=self.request.user, recipe_id__tags__title__in=get_request_tags(
                request=self.request)).select_related(
            'user').prefetch_related('recipe_id__tags').distinct()
        print(self.favorites)
        from django.db import connection
        print(connection.queries)
        return self.favorites

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context