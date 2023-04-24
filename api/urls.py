from django.contrib import admin
from django.urls import path
from api.views import UserRegistrationView, UserLoginView , UserProfileView, UserChangePasswordView,\
        UserSendPasswordResetView , UserPasswordResetView
urlpatterns = [
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('profile/', UserProfileView.as_view(), name='profile'),
        path('ChangePassword/', UserChangePasswordView.as_view(), name='ChangePassword'),
        path('SendEmailPasswordReset/', UserSendPasswordResetView.as_view(), name='SendEmailPasswordReset'),
        path('PasswordReset/<uid>/<token>/', UserPasswordResetView.as_view(), name='PasswordReset'),
]
