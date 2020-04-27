from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from core.permissions import PostPermission, CommentPermission
from core.models import Post, Event, Comment, CommentPost
from core.serializers import PostSerializer, PostDetailedSerializer, EventSerializer, EventDetailedSerializer, CommentPostSerializer, CommentPostDetailedSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (PostPermission, )

    def get_serializer_class(self):
        # if self.action == 'list':
        #     return PostSerializer
        return PostDetailedSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return serializer.data


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsAdminUser, )

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSerializer
        return EventDetailedSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer.data


class CommentPostViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (CommentPermission, )

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentPost
        return CommentPostDetailedSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer.data
