from django.contrib import admin
from .models import Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
