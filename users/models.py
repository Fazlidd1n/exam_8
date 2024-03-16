import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE, DateTimeField, ImageField, UUIDField



class UserPhoto(Model):
    user = ForeignKey('auth.User', CASCADE)
    image = ImageField(default='product/images/default.png', upload_to='')
    created_at = DateTimeField(auto_now_add=True)


class Category(Model):
    name = CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=50)
    price = IntegerField()
    description = CharField(max_length=255)
    category = ForeignKey('users.Category', CASCADE)
    user = ForeignKey('auth.User', CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductPhoto(Model):
    product = ForeignKey('users.Product', CASCADE)
    image = ImageField(default='product/images/default.png', upload_to='')
    created_at = DateTimeField(auto_now_add=True)

# User._meta.get_field('groups').remote_field.related_name = 'user_groups'
# User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions_set'
