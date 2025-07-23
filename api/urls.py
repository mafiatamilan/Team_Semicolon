<<<<<<< HEAD
from django.urls import path
from .views import UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
=======
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('users/', include('user.urls')),
    path('accounts/', include('accounts.urls')),  # if you have one
>>>>>>> 551e2cb (Updated Everythings)
]
