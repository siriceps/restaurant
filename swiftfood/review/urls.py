from rest_framework import routers
from .views import ReviewViewSet
from .views import Average
from .views import SumOfEachScore
from .views import CountReview


router = routers.DefaultRouter()
router.register(r'average', Average)
router.register(r'sum_of_each', SumOfEachScore)
router.register(r'count_score', CountReview)
router.register(r'', ReviewViewSet)


app_name = 'review'
urlpatterns = router.urls
