from django.urls import path, include
from auth_server.api.views.users.index import registerUser, deleteUser, updateUser, activateUser
from auth_server.api.views.auth.index import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', registerUser, name='register-user'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('delete/<int:pk>/', deleteUser, name='delete-user'),
    path('update/<int:pk>/', updateUser, name='update-user'),
    path('activate/<int:pk>/', activateUser, name='activate-user'),
]