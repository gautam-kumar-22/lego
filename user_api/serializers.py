from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    contact_number = serializers.IntegerField()
    address = serializers.CharField()
    user_profile = serializers.FileField()

    # def validate_username(self, username):
    #     try:
    #         user = User.objects.get(username=username)
    #         raise serializers.ValidationError("User does not exit with entered username.")
    #     except User.DoesNotExits:
    #         pass
    #     return username

    # def validate_email(self, email):
    #     try:
    #         user = User.objects.get(email=email)
    #         raise serializers.ValidationError("User does not exit with entered email.")
    #     except User.DoesNotExits:
    #         pass
    #     return email

    # def validate_password(self, password):
    #     if password == "":
    #         raise serializers.ValidationError("Fill the password field.")
    #     return password

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'contact_number', 'address', 'user_profile')

    def create(self, validated_data):
        user = User(email=validated_data.get('email'),
            username=validated_data.get('username'),
        )
        user.set_password(validated_data['password'])
        user.contact_number = validated_data.get('contact_number')
        user.address = validated_data.get('address')
        user_profile = validated_data.get('user_profile')
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError("Fill the password field.")
        return password

    def validate(self, data):
        username = data.get("username")
        password = self.validate_password(data.get('password'))
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExits:
            raise serializers.ValidationError("User does not exit with entered username.")
        authenticated_user = authenticate(username=user.username, password=password)
        if authenticated_user:
            data['authenticated_user'] = authenticated_user
        else:
            raise serializers.ValidationError("Invalid Credentials.")
        return data

    class Meta:
        model = User
        fields = ('username', 'password')
