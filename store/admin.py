from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery, ProductVideo
import admin_thumbnails
from django.utils.html import format_html


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'display_image', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.images.url))

    display_image.short_description = 'Image'

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category','variation_value','extra_cost', 'is_active')
    list_editable = ('is_active',)
    list_editable = ('extra_cost',)
    list_editable = ('variation_value',)
    list_filter = ('product', 'variation_category', 'variation_value','extra_cost')

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
admin.site.register(ProductVideo)
