import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__id', lookup_expr="iexact")
    class Meta:
        model = Product
        fields = ['description', "category"]