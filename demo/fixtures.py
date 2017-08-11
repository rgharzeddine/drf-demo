import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

import django
django.setup()

from drf.models import Invoice, Product, User as MyUser
from django.contrib.auth.models import User

if False:
    users = [
        MyUser(username='man', password='1234', role='manager'),
        MyUser(username='jawad', password='1234', role='accountant'),
        MyUser(username='imad', password='1234', role='salesman'),
    ]
    for user in users:
        user.save()

    print('database initialized !')

if True:
    # add some users
    users = [
        User(username='rawad'),
        User(username='admin'),
    ]
    for user in users:
        user.set_password('1234')
        user.save()

    print('users added !')

    # add some salesmen (to users table)
    salesmen = [
        User(username='imad'),
        User(username='ziad'),
    ]
    for user in salesmen:
        # user.set_password('1234')
        user.save()

    print('salesmen added !')

    # add some products
    rawad = User.objects.get(username='rawad')
    admin = User.objects.get(username='admin')

    products = [
        Product(name='car', price=10200, created_by=rawad),
        Product(name='carpet', price=200, created_by=admin),
        Product(name='cartridge', price=20, created_by=rawad),
    ]
    for product in products:
        product.save()

    print('products added !')

    # add some invoices
    imad = User.objects.get(username='imad')
    ziad = User.objects.get(username='ziad')

    invoices = [
        Invoice(type='In', amount=50000, salesman=imad, created_by=admin),
        Invoice(type='Out', amount=60000, salesman=ziad, created_by=admin),
        Invoice(type='In', amount=20500, salesman=ziad, created_by=rawad),
    ]
    for invoice in invoices:
        invoice.save()

    print('invoices added !')
