from django.contrib import admin
from .models import CustomUser, Product, Category, Order, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','category','created_at')
    search_fields = ('name',)
    list_filter = ('category', 'created_at')

class OrderAdmin(admin.ModelAdmin):
    list_display= ('id','user','total_price','status','created_at')
    list_filter= ('status',)

admin.site.register(CustomUser)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
# Register your models here.
