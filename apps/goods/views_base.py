# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/4/7 11:13'

from django.shortcuts import render
from django.views.generic.base import View

from goods.models import Goods


# 版本1
# class GoodsListView(View):
#     def get(self, request):
#         """
#         通过django的view实现商品列表页
#         :param request:
#         :return:
#         """
#         json_list = []
#         goods = Goods.objects.all()[:10]
#         # 接下来将goods返回成json
#         for good in goods:
#             json_dict = {}
#             json_dict['name'] = good.name
#             json_dict['category'] = good.category.name
#             json_dict['market_price'] = good.market_price
#             json_list.append(json_dict)
#
#         from django.http import HttpResponse
#         import json
#         return HttpResponse(json.dumps(json_list), content_type="application/json")


# 版本2
class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # 接下来将goods返回成json
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # 当字段过多，提取麻烦,下面方法可以直接将model转换成dict
        from django.forms.models import model_to_dict
        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        import json
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse

        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(json_data, safe=False)








