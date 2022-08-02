from django.urls import path, include
from .views import IndexListView, RecipeDetailView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('<slug:slug>/',
         RecipeDetailView.as_view(),
         name='recipe_view_slug')
]
