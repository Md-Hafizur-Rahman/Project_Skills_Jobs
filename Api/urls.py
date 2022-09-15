from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from Api.views import CouponViewSet,OrderViewSet,OrderItemViewSet

router.register(r'coupon', CouponViewSet,basename='coupon')
router.register(r'order', OrderViewSet,basename='order')
router.register(r'orderitem', OrderItemViewSet,basename='orderitem')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
