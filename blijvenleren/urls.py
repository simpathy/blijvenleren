from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResourceViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'resources', ResourceViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]