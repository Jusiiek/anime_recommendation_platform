from django.shortcuts import get_list_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import User, Role
from user.serializers import UserFrontendSerializer

from .serializers import MyTokenObtainPairSerializer, ChangePasswordSerializer, UpdateUserSerializer, \
    ResetPasswordSerializer, SetNewPasswordSerializer, RegisterSerializer

from logger import logger


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            **serializer.validated_data,
            **UserFrontendSerializer(serializer.user).data
        }, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):

        if not request['password']:
            return Response({"error": "Missing password"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            logger.warning(str(e))
            return Response({"errors": e.args[0]}, status=status.HTTP_200_OK)

        user = User.objects.create(**serializer.validated_data)
        user.set_password(request.data['password'])
        role = request.data["role"]
        role = Role.objects.get(name=role)
        user.set_role(role)
        user.save()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        if request.user.check_password(request.data['old_password']):
            request.user.set_password(request.data['password'])
            request.user.save()
            return Response({'success': 'Changed password'}, status=status.HTTP_200_OK)
        return Response({'error': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.warning(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {'success': 'We have sent you a link to reset your password'},
            status=status.HTTP_200_OK
        )


class SetNewPasswordApi(APIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = (AllowAny,)

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {'success': True, 'message': 'Password reset success'},
            status=status.HTTP_200_OK
        )
