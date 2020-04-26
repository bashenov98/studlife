from rest_framework import viewsets, status, mixins

from core.models import Post, Event, CommentPost

class PostViewSet(viewsets.ModelViewSet):
    queryset =