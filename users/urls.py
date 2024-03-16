from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from users.views import UserViewSet, UserCreateAPIView, CategoryListAPIView, ProductListCreateAPIView, \
    ProductRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('categories/', CategoryListAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view()),
    path('product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
