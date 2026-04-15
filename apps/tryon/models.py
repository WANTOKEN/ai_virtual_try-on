import uuid
from django.db import models
from django.conf import settings


class TryonRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clothing = models.ForeignKey('wardrobe.Clothing', on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='tryon/user/')
    result_image = models.ImageField(upload_to='tryon/result/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        db_table = 'tryon_records'