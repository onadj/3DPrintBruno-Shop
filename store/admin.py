from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
import admin_thumbnails
from django.utils.html import format_html
from import_export.formats import base_formats
from .models import Product, Variation, ReviewRating, ProductGallery, ProductVideo
from django.utils import timezone


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('id',)
        export_order = ('id', 'product_name', 'price', 'stock', 'category', 'is_available')
        skip_unchanged = True
        report_skipped = False
        use_bulk = True
        encoding = 'utf-8'
        formats = [base_formats.XLSX]


class VariationResource(resources.ModelResource):
    class Meta:
        model = Variation
        import_id_fields = ('id',)
        export_order = ('id', 'product', 'variation_category', 'variation_value', 'extra_cost', 'is_active')
        skip_unchanged = True
        report_skipped = False
        use_bulk = True
        encoding = 'utf-8'
        formats = [base_formats.XLSX]

class ReviewRatingResource(resources.ModelResource):
    class Meta:
        model = ReviewRating

class ProductGalleryResource(resources.ModelResource):
    class Meta:
        model = ProductGallery

class ProductVideoResource(resources.ModelResource):
    class Meta:
        model = ProductVideo
        
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('product_name', 'display_image', 'price', 'stock', 'category', 'description', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

    def display_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.images.url))
        else:
            return "No Image"

    display_image.short_description = 'Image'

    def description(self, obj):
        return obj.description

    description.short_description = 'Description'

class VariationAdmin(ImportExportModelAdmin):
    resource_class = VariationResource
    list_display = ('product', 'variation_category', 'variation_value', 'extra_cost', 'is_active')
    list_editable = ('is_active', 'extra_cost', 'variation_value')
    list_filter = ('product', 'variation_category', 'variation_value', 'extra_cost')

class ReviewRatingAdmin(ImportExportModelAdmin):
    resource_class = ReviewRatingResource

class ProductGalleryAdmin(ImportExportModelAdmin):
    resource_class = ProductGalleryResource

class ProductVideoAdmin(ImportExportModelAdmin):
    resource_class = ProductVideoResource

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery, ProductGalleryAdmin)
admin.site.register(ProductVideo, ProductVideoAdmin)
