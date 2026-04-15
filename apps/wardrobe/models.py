import uuid
from django.db import models
from django.conf import settings


class ClothingCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'clothing_categories'


class Clothing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ClothingCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothing/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clothing'