from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()

router.register('api/personas', 'personas')

urlpatterns = router.urls