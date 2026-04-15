from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MediaFile
from .serializers import MediaFileSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def upload(self, request):
        # Implement upload logic
        return Response({'message': 'Upload not implemented yet'})