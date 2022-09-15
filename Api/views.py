from django.contrib.auth.models import User
from rest_framework import  viewsets
from apps.order.models import Coupon, Order, OrderItem
from Api.serializer import CouponSerializer ,OrderSerializer,OrderItemSerializer

class CouponViewSet(viewsets.ModelViewSet):
    
    queryset = Coupon.objects.all()
    serializer_class =  CouponSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class =  OrderSerializer
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class =  OrderItemSerializer
