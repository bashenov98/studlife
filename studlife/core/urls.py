from django.urls import path, include
from core.views.viewsets import PostViewSet, EventViewSet, CommentPostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentPostViewSet)
router.register('events', EventViewSet)


urlpatterns = [] + router.urls
