def cart_summary(request):

    cart = request.session.get("shopping_cart", {})

    cart_count = sum(cart.values())

    return {
        "cart_count": cart_count
    }
def cart_summary(request):
    cart = request.session.get("shopping_cart", {})

    count = sum(
        int(quantity)
        for quantity in cart.values()
    )

    return {
        "cart_count": count
    }