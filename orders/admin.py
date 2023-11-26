# orders/admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Payment, Order, OrderProduct
from .resources import OrderResource
# admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Payment, Order, OrderProduct
from .resources import OrderResource

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'selected_variations', 'quantity', 'product_price', 'ordered')
    extra = 0

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at', 'product_names', 'get_selected_variations']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]
    resource_class = OrderResource  # Add this line

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        from import_export.resources import ModelResource
        from import_export.fields import Field
        from django.http import HttpResponse
        from django.utils.encoding import smart_str
        import csv

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=orders.csv'

        csv_writer = csv.writer(response)

        order_resource = OrderResource()

        header = order_resource.get_export_headers()
        csv_writer.writerow(header)

        for order in queryset:
            row_data = order_resource.export(Order.objects.filter(id=order.id))
            csv_writer.writerow([smart_str(field) for field in row_data])

        return response

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
