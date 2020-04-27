from django.urls import path, include
from core.views.viewsets import PostViewSet, EventViewSet, CommentPostViewSet
from core.views.fbv_views import posts, comments
from core.views.cbv_views import PostDetailAPIView,PostCreateUpdateAPIView, PostListAPIView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('postss', PostViewSet)
router.register('comments', CommentPostViewSet)
router.register('events', EventViewSet)


urlpatterns = [

    path('posts', posts),
    path('posts/<int:pk>/comments', comments),
    path('postcreate/',PostCreateUpdateAPIView.as_view()),
] + router.urls
