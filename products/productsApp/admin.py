from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','created_at']


#sonar 123456
#https://github.com/Ranoscyber/products_backend_api.git