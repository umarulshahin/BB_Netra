from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta: 
        
        model = OrderDetails
        fields = "__all__"
        
    def validate(self, attrs):

 
        if not attrs.get('product_code'):
            raise serializers.ValidationError("Product code is required.")
        
        if not attrs.get("OEM_no"): 
            raise serializers.ValidationError("OEM number is required.")
        
        if not attrs.get("quantity") or attrs.get("quantity") <= 0:
            raise serializers.ValidationError("Quantity must be a more than 0.")
        
        if not attrs.get("delivery_type"): 
            raise serializers.ValidationError("Delivery type is required.")
        
        if not attrs.get("packing_type") : 
            raise serializers.ValidationError("Packing type is required.")
        
        if attrs.get("delivery_type") not in [DeliveryType.AIR, DeliveryType.SEA]:
            raise serializers.ValidationError("Invalid delivery type. Choose either Air or Sea.")
        
        if attrs.get("packing_type") not in [PackingType.BOX, PackingType.TUBE]:
            raise serializers.ValidationError("Invalid packing type. Choose either Box or Tube.")
        
        return attrs
    
    def create(self, validated_data):
        
       order = OrderDetails.objects.create(**validated_data)
       return order
