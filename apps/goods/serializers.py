# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/4/7 12:21'

from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"






