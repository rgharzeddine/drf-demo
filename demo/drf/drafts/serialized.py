# run using python manage.py shell

from drf.models import User
from drf.serializers import UserSerializer
serializer = UserSerializer(User.objects.all(), many=True)
print(serializer.data)
