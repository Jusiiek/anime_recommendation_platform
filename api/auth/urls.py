from django.urls import path
from auth.views import MyObtainPairView, RegisterView, ChangePasswordView, LogoutView, \
RequestPasswordResetEmail, SetNewPasswordApi, UpdateProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('request_reset_email/', RequestPasswordResetEmail.as_view(), name='request_reset_email'),
    path('password_reset_complete/', SetNewPasswordApi.as_view(), name='password_reset_complete'),
]
