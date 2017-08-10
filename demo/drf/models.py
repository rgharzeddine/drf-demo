from django.db import models

from django.contrib.auth.models import User

IN = 'In'
OUT = 'Out'

INVOICE_TYPE = (
    (IN, 'in'),
    (OUT, 'out'),
)


# class User(models.Model):
#     user_pk = models.AutoField(primary_key=True)
#     username = models.TextField(blank=False, null=False)
#     password = models.TextField()
#     role = models.TextField(null=False, default='')

#     class Meta:
#         ordering = ('username',)

#     def __str__(self):
#         return 'user {} in role {}'.format(self.username, self.role)


class Product(models.Model):
    product_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField(default=0)
    dummy = models.TextField(default='')
    created_by = models.ForeignKey(
        User,
        related_name='product_created_by',
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
        related_name='invoice_salesman',
        on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User,
        related_name='invoice_created_by',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', 'type')
