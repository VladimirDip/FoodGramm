from django.urls import path, include
from .views import IndexListView
from .views import RecipeDetailView
from .views import FavoritesListView
from .views import RecipeCreateView
from .views import RecipeUpdateView
from .views import SubscriptionsListView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create_view'),
    path('detail/<slug:slug>/',
         RecipeDetailView.as_view(),
         name='recipe_view_slug'),
    path('detail/<slug:slug>/edit',
         RecipeUpdateView.as_view(),
         name='recipe_edit_view'),
    path('favorites/', FavoritesListView.as_view(), name='favorites'),
    path('subscriptions/', SubscriptionsListView.as_view(), name='subscriptions')
]
