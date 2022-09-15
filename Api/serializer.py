from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from apps.order.models import Coupon

class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'type','is_active', 'start_date', 'end_date','amount']