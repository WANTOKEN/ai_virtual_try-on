from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sms-login/', views.sms_login, name='sms_login'),
    path('send-sms/', views.send_sms, name='send_sms'),
    path('logout/', views.logout, name='logout'),
    path('me/', views.me, name='me'),
]