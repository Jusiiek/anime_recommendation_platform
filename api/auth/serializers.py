import jwt
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from api.user.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Login, generates a token to assigned to the user

    :return
    ------
    token : string - user token
    """

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_token(cls, user) -> str:
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    """
    User registration
    """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UpdateUserSerializer(serializers.ModelSerializer):
    """
    User updating
    """

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username']

    def validate_email(self, value: str) -> str:
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value: str) -> str:
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You don't have permission for this user."})

        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.save()
        return instance


class ResetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField(min_length=2)
    url = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['email', 'url', 'id']

    def validate(self, attrs: dict) -> dict:
        request = self.context['request']
        email = request.data['email']
        url = request.data['url']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

