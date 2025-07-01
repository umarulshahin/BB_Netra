from django.db import models
from Authentication_app.models import CustomUser
from django.utils import timezone
import uuid
import os
# Create your models here.

def truncate_filename(instance, filename, subfolder):
    filename_base, filename_ext = os.path.splitext(filename)
    truncated_filename = filename_base[:100] + filename_ext
    return os.path.join('img', subfolder, truncated_filename)

def upload_product_image(instance, filename):
    return truncate_filename(instance, filename, 'profile')
class DeliveryType(models.TextChoices):
    AIR = 'AIR', 'Air'
    SEA = 'SEA', 'Sea'

class PackingType(models.TextChoices):
    BOX = 'BOX', 'Box'
    TUBE = 'TUBE', 'Tube'
    
class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    SHIPPED = 'SHIPPED', 'Shipped'
    DELIVERED = 'DELIVERED', 'Delivered'
class OrderDetails(models.Model): 
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='orders')
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_code = models.CharField(max_length=255, null=True, blank=True)
    OEM_no = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    urgency = models.BooleanField(default=False, null=False, blank=False)
    comments = models.TextField(null=True, blank=True)
    delivery_type = models.CharField(max_length=10, choices=DeliveryType.choices, null=False, blank=False)
    packing_type = models.CharField(max_length=10, choices=PackingType.choices, null=True, blank=True)
    marking_instructions = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to=upload_product_image, null=True, blank=True)
    order_status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)