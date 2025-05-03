from rest_framework import serializers
from .models import *
import re


#............................................Registration serializer............................................
class RegistrationSerializer(serializers.ModelSerializer):
    
    con_password = serializers.CharField(write_only=True)
    class Meta: 
        model = CustomUser
        fields = ['email', 'username', 'password', 'con_password']
        read_only_fields = ['user_id']
        extra_kwargs = {'con_password' : {'write_only': True}}
        
    #........................ validation for email, username and password........................
    def validate(self, attrs):
        
        username_pattern = r'^(?=.{3,}$)[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$'
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        
        if not re.match(username_pattern, attrs['username']):
            raise serializers.ValidationError({'error':'Invalid Username.Username must contain atleast 3 characters and must start with a letter'})
        elif not re.match(email_pattern, attrs['email']):
            raise serializers.ValidationError({'error':'Invalid Email format'})
        elif not re.match(password_pattern, attrs['password']): 
            raise serializers.ValidationError({'error':'Invalid Password . Password must contain atleast 8 characters, 1 uppercase, 1 digit and 1 special character'})
        elif attrs['password'] != attrs['con_password']:
            raise serializers.ValidationError({'error':'Password does not match'})
        return attrs
    
    #........................ creating user........................
    def create(self, validated_data):
        
        user = CustomUser.objects.create_user(email=validated_data['email'], 
                                              username=validated_data['username'],
                                              password=validated_data['password'])
        user.save()
        return user