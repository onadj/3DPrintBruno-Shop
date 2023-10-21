from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    total_cost = 0  # Initialize total_cost to zero

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            
            for cart_item in cart_items:
                cart_count += cart_item.quantity

                # Calculate and add the extra cost for each variation
                extra_cost = 0
                for variation in cart_item.variations.all():
                    extra_cost += variation.extra_cost
                total_cost += (cart_item.product.price + extra_cost) * cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count, total_cost=total_cost)
