from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin,MPTTModelAdmin

# Register your models here.
from .models import Category, Coment, Images, Product, ShopCart


# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 4
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['tittle','status']
    list_filter = ['status']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'status','price','image_tag','amount']
    readonly_fields = ('image_tag',)
    list_filter = ['status']
    inline = [ProductImageInline]
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['tittle','product','image']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "tittle"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields={'slug':('tittle',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ComentAdmin(admin.ModelAdmin):
    list_display = ['subject','status','user','product','comment']
    list_filter = ['status']


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Coment)
admin.site.register(ShopCart,ShopCartAdmin)
