from drf.models import Invoice, Product, User
if False:
    users = [
        User(username='man', password='1234', role='manager'),
        User(username='jawad', password='1234', role='accountant'),
        User(username='imad', password='1234', role='salesman'),
    ]
    for user in users:
        user.save()

    print('database initialized !')
