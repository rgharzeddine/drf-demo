from django.db import models
from django.contrib.auth.models import User

IN = 'In'
OUT = 'Out'

INVOICE_TYPE = (
    (IN, 'in'),
    (OUT, 'out'),
)


class Product(models.Model):
    product_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField(default=0)
    dummy = models.TextField(default='')
    created_by = models.ForeignKey(
        User,
        related_name='user_products',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)


class Invoice(models.Model):
    invoice_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.TextField(default=IN, choices=INVOICE_TYPE)
    amount = models.FloatField(default=0)
    dummy = models.TextField(default='')
    salesman = models.ForeignKey(
        User,
        related_name='salesman_invoices',
        on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User,
        related_name='user_invoices',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', 'type')
