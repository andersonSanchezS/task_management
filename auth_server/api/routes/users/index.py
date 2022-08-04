from django.urls import path, include
from auth_server.api.views.users.index import registerUser, deleteUser, updateUser, activateUser
from auth_server.api.views.auth.index import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register', registerUser, name='register-user'),
    path('login', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('verify', TokenVerifyView.as_view(), name='verify'),
    path('delete', deleteUser, name='delete-user'),
    path('update', updateUser, name='update-user'),
    path('activate', activateUser, name='activate-user'),
]