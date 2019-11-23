from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets

from users.serializers.users import UserSerializer, GroupSerializer

__all__ = (
    'UserViewSet',
    'GroupViewSet',
)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
