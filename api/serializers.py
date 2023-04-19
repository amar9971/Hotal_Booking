from rest_framework import serializers
from api.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'mobile_no', 'tc', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }


def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
        raise serializers.ValidationError("password and confirm password does not match")

    return attrs


def create(self, validate_data):
    return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = {'email', 'password'}
