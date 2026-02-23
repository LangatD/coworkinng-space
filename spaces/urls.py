from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoworkingSpaceViewSet

router = DefaultRouter()
router.register(r'spaces', CoworkingSpaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]