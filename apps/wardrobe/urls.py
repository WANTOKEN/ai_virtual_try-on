from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clothing', views.ClothingViewSet)
router.register(r'categories', views.ClothingCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]