from rest_framework import routers

from exercises import apis as exercises
from trainers import apis as trainers
from users import apis as users

__all__ = (
    'router',
)

router = routers.DefaultRouter()
router.register(r'exercises', exercises.ExerciseViewSet)
router.register(r'exercise_categories', exercises.ExerciseCategoryViewSet)
router.register(r'users', users.UserViewSet)
router.register(r'groups', users.GroupViewSet)
router.register(r'trainers', trainers.TrainerViewSet)
