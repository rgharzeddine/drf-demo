from .models import Product, Invoice, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_pk', 'username', 'password', 'role', )


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('product_pk', 'name', 'type', 'amount', 'dummy', 'salesman', 'created_by', 'created_at', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('invoice_pk', 'name', 'price', 'dummy', 'created_by', 'created_at', )
