from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from users.serializers.users import UserSerializer, GroupSerializer

__all__ = (
    'UserViewSet',
    'GroupViewSet',
)

User = get_user_model()


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='User List',
        operation_description='유저 목록',
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Get User',
        operation_description='유저 한명',
    )
)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    swagger_schema = None

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='Group List',
        operation_description='그룹 목록',
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Get Group',
        operation_description='그룹 하나',
    )
)
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    swagger_schema = None

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
