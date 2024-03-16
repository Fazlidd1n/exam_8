from django.contrib.auth.models import User
from django.core.mail import send_mail
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from exam_8 import settings
from users.filters import CategoryFilter
from users.models import Product, Category
from users.permissions import OwnProfilePermission
from users.serializers import UserModelSerializer, UserRegisterModelSerializer, ProductModelSerializer, \
    ProductDetailModelSerializer, CategoryModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    filter_backends = (OrderingFilter, DjangoFilterBackend, SearchFilter)
    ordering_fields = ('id', 'username')
    search_fields = ('username', 'email')
    filterset_fields = ('username', 'is_staff')

    @action(detail=False, methods=['GET'], url_path='get-me')
    def get_me(self, request, pk=None):
        if request.user.is_authenticated:
            return Response({'message': f'{request.user.username}'})
        return Response({'message': 'login qilinmagan'})


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        email_subject = "Register Project"
        email_message = 'Success rigester ✅'
        send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [user.email])
        return Response({'message': 'success send email message !'}, status=status.HTTP_201_CREATED)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filterset_class = CategoryFilter
    filter_backends = [SearchFilter]


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    search_fields = ['name', 'description']
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailModelSerializer
    permission_classes = (IsAuthenticated, OwnProfilePermission)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
