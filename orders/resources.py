# orders/resources.py
from import_export import resources, fields
from .models import Order

class OrderResource(resources.ModelResource):
    product_names = fields.Field(column_name='product_names', attribute='product_names')
    selected_variations = fields.Field(column_name='selected_variations', attribute='selected_variations')
    full_name = fields.Field(column_name='full_name', attribute='full_name')
    address = fields.Field(column_name='address', attribute='full_address')  # Assuming you have a 'full_address' method in your Order model

    class Meta:
        model = Order
        fields = ('order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at', 'product_names', 'selected_variations')

    def dehydrate_product_names(self, order):
        return order.product_names

    def dehydrate_selected_variations(self, order):
        return order.selected_variations
