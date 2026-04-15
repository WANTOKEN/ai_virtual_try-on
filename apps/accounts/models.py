from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)
    sms_code = models.CharField(max_length=6, blank=True, null=True)
    sms_code_expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'users'