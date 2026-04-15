from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Clothing, ClothingCategory
from .serializers import ClothingSerializer, ClothingCategorySerializer


class ClothingViewSet(viewsets.ModelViewSet):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def upload(self, request):
        # Implement upload logic
        return Response({'message': 'Upload not implemented yet'})


class ClothingCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClothingCategory.objects.all()
    serializer_class = ClothingCategorySerializer