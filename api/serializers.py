from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Username is already taken."})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email is already registered."})

        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # remove password2 since it's not in the User model
        user = User.objects.create_user(**validated_data)  # this hashes the password properly
        return user
