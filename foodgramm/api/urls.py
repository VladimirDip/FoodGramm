from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import IngredientViewSet, FavoriteViewSet, SubsrtiptionViweSet

router_v1 = DefaultRouter()
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')
router_v1.register(r'favorites',
                   FavoriteViewSet,
                   basename='favorites')
router_v1.register(r'subscriptions', SubsrtiptionViweSet, basename='subscriptions')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]