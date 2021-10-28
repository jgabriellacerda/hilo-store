from django.contrib import admin
from core.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('user',)

admin.site.register(Product, ProductAdmin)