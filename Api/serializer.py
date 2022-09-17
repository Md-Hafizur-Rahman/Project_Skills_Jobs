from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from apps.order.models import Coupon,Order,OrderItem

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'type','is_active', 'start_date', 'end_date','amount']
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product','unit', 'qty', 'price']
class OrderSerializer(serializers.ModelSerializer):
    order_item=OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['code','amount', 'coupon', 'discount','total','date','status','payment','tnx_id','payment_type','order_item']
