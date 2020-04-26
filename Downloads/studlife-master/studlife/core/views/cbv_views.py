from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from ..models import Post, Event, CommentPost
from ..serializers import PostSerializer, PostDetailedSerializer, EventSerializer, EventDetailedSerializer, CommentPostSerializer, CommentPostDetailedSerializer
from ..permissions import PostPermission, EventPermission, CommentPermission
from rest_framework import mixins


class PostListAPIView(mixins.ListModelMixin,
                        generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetailAPIView(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailedSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostCreateUpdateAPIView(mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                                generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
