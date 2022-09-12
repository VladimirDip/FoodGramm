from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from api.models import Favorites, Subscriptions, Purchases
from .logic import get_request_tags, save_recipe, edit_recipe, purchases_download
from .models import Recipe, Tag
from .forms import RecipeForm

User = get_user_model()


@login_required
def purchases_download_by(request):
    list_download = purchases_download(request=request)
    return list_download


class DataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


class IndexListView(DataMixin, ListView):
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


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'singlePage.html'
    context_object_name = 'recipe'


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


class AuthorRecipes(DataMixin, ListView):
    model = Recipe
    template_name = 'authorRecipe.html'
    context_object_name = 'author_recipes'
    paginate_by = 2

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs['author_name'])
        self.author_recipes = Recipe.objects.filter(tags__title__in=get_request_tags(
            request=self.request), author=author).select_related(
            'author').prefetch_related('tags').distinct()
        return self.author_recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_object_or_404(User, username=self.kwargs['author_name'])
        return context


class FavoritesListView(DataMixin, ListView):
    model = Favorites
    context_object_name = 'favorites'
    paginate_by = 3
    template_name = 'favorite.html'

    def get_queryset(self):
        self.favorites = Favorites.objects.filter(
            user_id=self.request.user, recipe_id__tags__title__in=get_request_tags(
                request=self.request)).select_related(
            'user').prefetch_related('recipe_id__tags').distinct()
        return self.favorites


class SubscriptionsListView(ListView):
    model = Subscriptions
    context_object_name = 'subscriptions'
    paginate_by = 3
    template_name = 'myFollow.html'

    def get_queryset(self):
        self.subscriptions = User.objects.filter(
            following__user=self.request.user).prefetch_related('recipes').annotate(
            recipe_count=Count('recipes')).order_by('username')
        return self.subscriptions


class ShopListView(ListView):
    model = Purchases
    context_object_name = 'purchases'
    paginate_by = 3
    template_name = 'shopList.html'
