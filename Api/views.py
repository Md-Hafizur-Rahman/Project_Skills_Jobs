from django.contrib.auth.models import User
from rest_framework import  viewsets
from apps.order.models import Coupon
from Api.serializer import CouponSerializer 

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class =  CouponSerializer
