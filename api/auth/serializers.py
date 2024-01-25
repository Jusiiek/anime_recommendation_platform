import jwt
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.password_validation import validate_password

from config import settings

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


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    change password for user
    """
    password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password')

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


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
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            absurl = f"{url}/{uidb64}/{RefreshToken.for_user(user)}"
        #     TODO add sens email
        return super().validate(attrs)


class SetNewPasswordSerializer(serializers.ModelSerializer):
    """
        set new password
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'token')

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            repeat_password = attrs.get('password2')
            token = attrs.get('token')

            user_id = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])['user_id']
            user = User.objects.get(id=user_id)

            if not user:
                raise serializers.ValidationError({"error": "Invalid reset password link"})
            if password != repeat_password:
                raise serializers.ValidationError({"password": "Password fields didn't match."})

            user.set_password(password)
            user.save()
            return token
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
