# _*_ coding: utf-8 _*_

import django_filters

from .models import Goods


class ProductFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    price_mix = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    # 模糊查询
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_mix', 'price_max',]
