from django.urls import path, include
from rest_framework import routers
from .views import *
from .api import *

router = routers.DefaultRouter()
router.register('capitan', CapitanViewSet, "capitan")
router.register(r'airplane', AirplaneViewSet)
router.register('company', CompanyViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', Main.as_view()),
]
