from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from users.models import Product, Category


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'password', 'date_joined')


class UserCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email', 'password'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, password):
        return make_password(password)


class UserRegisterModelSerializer(ModelSerializer):
    password_confirm = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise ValidationError("Error password")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ProductModelSerializer(ModelSerializer):
    # user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'category', 'user')


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category')
