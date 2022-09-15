from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from Api.views import CouponViewSet
router.register(r'coupon', CouponViewSet,basename='coupon')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
