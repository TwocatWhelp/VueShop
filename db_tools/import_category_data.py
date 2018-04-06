# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/4/6 15:23'


# 独立使用django的model

import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
# pwd = os.getcwd()
#  这种方法更简便，为了与教程一致性，用上一种
sys.path.append(pwd + "../")

# 如果想单独使用model，需要设置环境变量，这个变量是早manage.py文件中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django
django.setup()

from goods.models import GoodsCategory

from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_intance = GoodsCategory()
    lev1_intance.code = lev1_cat['code']
    lev1_intance.name = lev1_cat['name']
    lev1_intance.category_type = 1
    lev1_intance.save()

    for lev2_cat in lev1_cat['sub_categorys']:
        lev2_intance = GoodsCategory()
        lev2_intance.code = lev2_cat['code']
        lev2_intance.name = lev2_cat['name']
        lev2_intance.parent_category = lev1_intance
        lev2_intance.category_type = 2
        lev2_intance.save()

        for lev3_cat in lev2_cat['sub_categorys']:
            lev3_intance = GoodsCategory()
            lev3_intance.code = lev3_cat['code']
            lev3_intance.name = lev3_cat['name']
            lev3_intance.parent_category = lev2_intance
            lev3_intance.category_type = 3
            lev3_intance.save()










