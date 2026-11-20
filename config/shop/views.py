
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Product
from .cart import get_cart


def product_list(request):
    products = Product.objects.filter(
        is_available=True,
        stock__gt=0
    )

    return render(
        request,
        "shop/product_list.html",
        {"products": products}
    )


@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True
    )

    cart = request.session.get("shopping_cart", {})
    product_id = str(product_id)

    current_quantity = int(cart.get(product_id, 0))

    if current_quantity >= product.stock:
        messages.warning(
            request,
            f"Only {product.stock} units of {product.name} are available."
        )
    else:
        cart[product_id] = current_quantity + 1
        request.session["shopping_cart"] = cart

        messages.success(
            request,
            f"{product.name} added to your cart!"
        )

    return redirect("shop:product_list")


def cart_detail(request):
    items, total = get_cart(request)

    return render(
        request,
        "shop/cart_detail.html",
        {
            "items": items,
            "total": total,
        }
    )


@require_POST
def cart_update(request, product_id):
    cart = request.session.get("shopping_cart", {})
    product_id = str(product_id)

    try:
        quantity = int(request.POST.get("quantity", 0))
    except (ValueError, TypeError):
        messages.error(request, "Please enter a valid quantity.")
        return redirect("shop:cart_detail")

    product = Product.objects.filter(
        id=product_id,
        is_available=True
    ).first()

    if not product:
        cart.pop(product_id, None)
        messages.warning(request, "This product is no longer available.")

    elif quantity <= 0:
        cart.pop(product_id, None)
        messages.success(request, "Product removed from cart.")

    elif quantity > product.stock:
        cart[product_id] = product.stock
        messages.warning(
            request,
            f"Only {product.stock} units are available."
        )

    else:
        cart[product_id] = quantity
        messages.success(request, "Cart updated successfully.")

    request.session["shopping_cart"] = cart

    return redirect("shop:cart_detail")
from django.shortcuts import render
def home(request):
    return render(request, 'shop/home.html')