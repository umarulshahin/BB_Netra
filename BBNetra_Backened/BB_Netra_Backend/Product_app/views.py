from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,APIView 
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import ProductSerializer

import logging

logger = logging.getLogger(__name__)

# Create your views here.


class Order_Management(APIView):
    
    
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request): 
        
        return Response({"message": "GET request received"}, status=status.HTTP_200_OK)
    
    def post(self, request): 
        
        data = request.data
        if not data: 
            raise ValueError("No data provided in the request. Please provide the necessary data.", status=status.HTTP_400_BAD_REQUEST)
        
        data['user'] = request.user.id
        
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info("Received data: %s", data)

            return Response({"Success": "Order created successfully"}, status=status.HTTP_201_CREATED)
        
        else: 
            return ValueError(serializer.errors, status = status.HTTP_400_BAD_REQUEST)