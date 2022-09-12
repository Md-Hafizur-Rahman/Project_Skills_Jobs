from django.contrib import admin
from apps.product.models import Category, Color,Product, Size,ProductPhoto
# Register your models her
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","photo","serial","slug",)
    
@admin.register(Color)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)
@admin.register(Size)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name","slug","catagory","price","colors","sizes","photo")
@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ("product","photo")
