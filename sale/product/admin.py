from django.contrib import admin
from product.models import ProductBrand, Product


class ProductBrandAdmin(admin.ModelAdmin):
    # 列表中的列
    list_display = ['id', 'name', 'create_time', 'update_time']
    # 搜索框
    search_fields = ['name', 'create_time', 'update_time']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product_brand', 'inventory', 'describe', 'price',
                    'create_time', 'update_time']
    # 搜索框
    search_fields = ['id', 'title', 'good_type', 'price']


admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'Sales Management System'

admin.site.site_title = 'Sales Management System'
