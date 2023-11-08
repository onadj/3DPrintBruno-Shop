# Import necessary modules
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from decimal import Decimal  # Import Decimal data type

# Function to get the cart ID from the session
def _cart_id(request):
    # Get or create a cart session key
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# Function to add items to the cart
def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)

    # Check if the user is authenticated (logged in)
    if current_user.is_authenticated:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    # Get the selected product variations
                    variation = Variation.objects.get(
                        product=product,
                        variation_category__iexact=key,
                        variation_value__iexact=value
                    )
                    product_variation.append(variation)
                except:
                    pass

        # Check if the cart item exists for the authenticated user
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user=current_user)

            for item in cart_item:
                existing_variation = item.variations.all()
                if list(existing_variation) == product_variation:
                    item.quantity += 1
                    item.save()
                    break
            else:
                # Create a new cart item with variations
                item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    user=current_user
                )
                item.variations.set(product_variation)
                item.save()
        else:
            # Create a new cart item for the authenticated user
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                user=current_user
            )
            cart_item.variations.set(product_variation)
            cart_item.save()
        return redirect('cart')
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    # Get the selected product variations
                    variation = Variation.objects.get(
                        product=product,
                        variation_category__iexact=key,
                        variation_value__iexact=value
                    )
                    product_variation.append(variation)
                except:
                    pass

        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=_cart_id(request)
            )
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, cart=cart)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)

            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                # Create a new cart item with variations
                item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    cart=cart
                )
                item.variations.set(product_variation)
                item.save()
        else:
            # Create a new cart item for non-authenticated users
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )
            cart_item.variations.set(product_variation)
            cart_item.save()
        return redirect('cart')

# Function to remove an item from the cart
def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # Delete the cart item if quantity is 1
            cart_item.delete()
    except:
        pass
    return redirect('cart')

# Function to remove a cart item
def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    # Delete the cart item
    cart_item.delete()
    return redirect('cart')

# Function to display the cart
def cart(request, total=Decimal('0'), quantity=0, cart_items=None, tax=Decimal('0'), grand_total=Decimal('0')):
    extra_costs = {}

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            base_price = Decimal(cart_item.product.price)
            quantity = cart_item.quantity
            extra_cost = sum([Decimal(variation.extra_cost) for variation in cart_item.variations.all()])
            subtotal = (base_price + extra_cost) * quantity

            total += subtotal
            quantity += cart_item.quantity
            extra_costs[cart_item.id] = extra_cost
            cart_item.subtotal = subtotal  # Store the subtotal in the cart_item

        tax = Decimal('7.99') 
        grand_total = total + tax  # Calculate grand total as the sum of total and tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'extra_costs': extra_costs,
    }
    return render(request, 'store/cart.html', context)

# Function for the checkout page
@login_required(login_url='login')
# Function for the checkout page
@login_required(login_url='login')
def checkout(request):
    total = Decimal('0')
    quantity = 0
    cart_items = None
    tax = Decimal('0')
    grand_total = Decimal('0')
    extra_costs = {}

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            base_price = Decimal(cart_item.product.price)
            quantity = cart_item.quantity
            extra_cost = sum([Decimal(variation.extra_cost) for variation in cart_item.variations.all()])
            subtotal = (base_price + extra_cost) * quantity

            total = subtotal
            quantity += cart_item.quantity
            extra_costs[cart_item.id] = extra_cost
            cart_item.subtotal = subtotal  # Store the subtotal in the cart_item

        tax = Decimal('7.99') 
        grand_total = total + tax  # Calculate grand total as the sum of total and tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'extra_costs': extra_costs,
    }

    return render(request, 'store/checkout.html', context)