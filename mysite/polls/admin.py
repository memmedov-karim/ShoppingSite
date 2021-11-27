from django.contrib import admin
from .models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'status']
    list_filter = ['status']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'status','price','amount']
    list_filter = ['status']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
