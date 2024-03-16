import django_filters
from django_filters import FilterSet
from .models import Category


class CategoryFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']
