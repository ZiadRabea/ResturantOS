import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['description']