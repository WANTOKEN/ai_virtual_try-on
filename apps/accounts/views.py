from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'phone': user.phone,
            }
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def sms_login(request):
    phone = request.data.get('phone')
    sms_code = request.data.get('sms_code')
    # Implement SMS verification logic
    return Response({'message': 'SMS login not implemented yet'})


@api_view(['POST'])
@permission_classes([AllowAny])
def send_sms(request):
    phone = request.data.get('phone')
    # Implement SMS sending logic
    return Response({'message': 'SMS sent'})


@api_view(['POST'])
def logout(request):
    # Invalidate token on client side
    return Response({'message': 'Logged out'})


@api_view(['GET'])
def me(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'phone': user.phone,
    })