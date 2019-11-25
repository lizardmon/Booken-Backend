from books import apis as books
from exercises import apis as exercises
from rest_framework import routers
from trainers import apis as trainers
from users import apis as users

__all__ = (
    'router',
)

router = routers.DefaultRouter()
router.register(r'books', books.BookViewSet)
router.register(r'exercises', exercises.ExerciseViewSet)
router.register(r'exercise_categories', exercises.ExerciseCategoryViewSet)
router.register(r'users', users.UserViewSet)
router.register(r'groups', users.GroupViewSet)
router.register(r'trainers', trainers.TrainerViewSet)
