from django.urls import path, include
from .views import IndexListView, RecipeDetailView, recipe_new

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('create/', recipe_new, name='recipe_create_view'),
    path('detail/<slug:slug>/',
         RecipeDetailView.as_view(),
         name='recipe_view_slug'),
]
