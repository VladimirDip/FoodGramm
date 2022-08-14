from django.urls import path, include
from .views import IndexListView, RecipeDetailView, FavoritesListView, RecipeCreateView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create_view'),
    path('detail/<slug:slug>/',
         RecipeDetailView.as_view(),
         name='recipe_view_slug'),
    path('favorites/', FavoritesListView.as_view(), name='favorites')
]
