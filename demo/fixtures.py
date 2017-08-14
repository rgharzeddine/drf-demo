import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

import django
django.setup()

from drf.models import Invoice, Product, User

if True:
    users = [
        User(username='admin'),
        User(username='rawad'),
        User(username='imad'),
        User(username='ziad'),
    ]
    for user in users:
        user.set_password('1234')
        user.save()

    print('users added !')

    admin = User.objects.get(username='admin')
    rawad = User.objects.get(username='rawad')
    imad = User.objects.get(username='imad')
    ziad = User.objects.get(username='ziad')

    # add some products
    Product.objects.bulk_create([
        Product(name='car', price=10200, created_by=rawad),
        Product(name='carpet', price=200, created_by=admin),
        Product(name='cartridge', price=20, created_by=rawad),
    ])
    print('products added !')

    # add some invoices
    Invoice.objects.bulk_create([
        Invoice(type='In', amount=50000, salesman=imad, created_by=admin),
        Invoice(type='Out', amount=60000, salesman=ziad, created_by=admin),
        Invoice(type='In', amount=20500, salesman=ziad, created_by=rawad),
    ])
    print('invoices added !')
