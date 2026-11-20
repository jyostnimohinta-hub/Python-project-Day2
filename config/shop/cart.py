from decimal import Decimal
from .models import Product


def get_cart(request):
    cart = request.session.get("shopping_cart", {})
    items = []
    total = Decimal("0.00")

    for product_id, quantity in list(cart.items()):

        try:
            product = Product.objects.get(
                id=product_id,
                is_available=True
            )

            quantity = int(quantity)

            if quantity <= 0:
                cart.pop(product_id, None)
                continue

            # Do not allow quantity above available stock
            quantity = min(quantity, product.stock)

            if quantity == 0:
                cart.pop(product_id, None)
                continue

            cart[product_id] = quantity

            line_total = product.price * quantity

            items.append({
                "product": product,
                "quantity": quantity,
                "line_total": line_total
            })

            total += line_total

        except (Product.DoesNotExist, ValueError, TypeError):
            cart.pop(product_id, None)

    request.session["shopping_cart"] = cart

    return items, total
