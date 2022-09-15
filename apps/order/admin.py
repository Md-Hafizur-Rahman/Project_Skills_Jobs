from django.contrib import admin
from apps.order.models import Coupon,Order,OrderItem

# Register your models here.
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code","amount",'type','start_date','end_date','is_active')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer","code","amount",'coupon','discount','total','date','status','payment','tnx_id','payment_type')
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order","product","qty",'price')