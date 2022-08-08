from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import IngredientViewSet

router_v1 = DefaultRouter()
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]