
from django.urls import path
from . import views


app_name = "shop"

urlpatterns = [
    # Display all available products
    path(
        "",
        views.product_list,
        name="product_list"
    ),

    # Add a product to the cart
    path(
        "cart/add/<int:product_id>/",
        views.cart_add,
        name="cart_add"
    ),

    # Display the shopping cart
    path(
        "cart/",
        views.cart_detail,
        name="cart_detail"
    ),

    # Update product quantity in the cart
    path(
        "cart/update/<int:product_id>/",
        views.cart_update,
        name="cart_update"
    ),
    path('', views.home, name='home'),
]

