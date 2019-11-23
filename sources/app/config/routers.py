from rest_framework import routers

from trainers import apis as trainers
from users import apis as users

__all__ = (
    'router',
)

router = routers.DefaultRouter()
router.register(r'users', users.UserViewSet)
router.register(r'groups', users.GroupViewSet)
router.register(r'trainers', trainers.TrainerViewSet)
