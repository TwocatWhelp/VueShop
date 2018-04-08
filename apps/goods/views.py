from goods.filters import ProductFilter
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from .models import Goods, GoodsCategory

# Create your views here.


# class GoodsListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serialize = GoodsSerializer(goods, many=True)
#         return Response(goods_serialize.data)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# 手动设置列表分页
class GoodsPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     # 手动分页
#     pagination_class = GoodsPagination


class GoodsListViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 手动分页
    pagination_class = GoodsPagination

    # 过滤功能
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filter_fields = ('name', 'shop_price')
    # 自定义过滤，可以从name, desc中过滤，甚至可以模糊搜索
    filter_class = ProductFilter
    # 搜索功能是最好的模糊搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 排序
    ordering_fields = ('add_time',)

    # 查询
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.objects.filter(shop_price__gt=int(price_min))
    #     return queryset


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List:
         商品分类列表数据
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer



