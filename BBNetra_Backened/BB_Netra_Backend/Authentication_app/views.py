from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


#............................................Registration............................................
@api_view(['POST'])
def Registration(request): 
    
    data = request.data
    print(data, 'data')
    
    if not data: 
        return Response('Please provide required fields', status=status.HTTP_400_BAD_REQUEST)
    
    serializer = RegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
    else : 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#............................................Login using email and password and genarate jwt token..............................................
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token["role"]=user.is_superuser
        
        return token

class MyTokenobtainedPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer