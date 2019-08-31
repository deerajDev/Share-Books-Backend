from django.contrib.auth  import authenticate
from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id','email','password','college','contact_num']
        extra_kwargs = {'password':{'write_only':True}}
    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=20,required=True , style={'input_type':'password','placeholder':'password'})
    #setting for password field
    extra_kwargs = {'password':{'style' : {'input_type': 'password', 'placeholder': 'Password'}, 'write_only':True}}

    def validate(self,data):
        print(data['email'], data['password'])
        user = authenticate(email=data['email'], password=data['password'])
        print(user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect email or password')