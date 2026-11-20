from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Product
from .serializers import ProductSerializer


class ProductPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]