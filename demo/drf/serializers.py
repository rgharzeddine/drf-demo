from drf import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username')  # 'password'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = ('invoice_pk', 'name', 'type', 'amount', 'dummy', 'salesman', 'created_by', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('product_pk', 'name', 'price', 'dummy', 'created_by', 'created_at')
