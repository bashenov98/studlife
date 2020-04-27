import logging
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView

from core.models import Post, CommentPost
from core.serializers import PostSerializer, CommentPostSerializer

@api_view(['GET'])
def posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def comments(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = CommentPost.objects.filter(post=post)
    serializer = CommentPostSerializer(comments,
                                            many=True,
                                            context={'request': request})
    return Response(serializer.data)