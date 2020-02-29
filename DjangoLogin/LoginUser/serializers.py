"""
用户对接返回的数据  进行序列化

"""
from rest_framework import serializers
from .models import Goods

class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields= ["id","goods_number","goods_name","goods_price","goods_count",
                 "goods_location","goods_safe_date","goods_status"]










