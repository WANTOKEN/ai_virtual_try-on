from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'records', views.TryonRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate/', views.TryonRecordViewSet.as_view({'post': 'generate'}), name='generate'),
]