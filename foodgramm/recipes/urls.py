from django.urls import path, include
from .views import IndexListView
from .views import RecipeDetailView
from .views import FavoritesListView
from .views import RecipeCreateView
from .views import RecipeUpdateView
from .views import SubscriptionsListView
from .views import AuthorRecipes
from .views import ShopListView
from .views import purchases_download_by

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
    path('subscriptions/', SubscriptionsListView.as_view(), name='subscriptions'),
    path('author/<str:author_name>/', AuthorRecipes.as_view(), name='author_recipes'),
    path('purchases/', ShopListView.as_view(), name='purchases'),
    path('download/', purchases_download_by, name='purchases_download')
]
