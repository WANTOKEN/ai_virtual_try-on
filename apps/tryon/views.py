from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TryonRecord
from .serializers import TryonRecordSerializer


class TryonRecordViewSet(viewsets.ModelViewSet):
    queryset = TryonRecord.objects.all()
    serializer_class = TryonRecordSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def generate(self, request):
        # Implement tryon generation logic
        return Response({'message': 'Generation not implemented yet'})

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        record = self.get_object()
        return Response({'status': record.status})

    @action(detail=True, methods=['post'])
    def save(self, request, pk=None):
        record = self.get_object()
        record.is_favorite = not record.is_favorite
        record.save()
        return Response({'is_favorite': record.is_favorite})