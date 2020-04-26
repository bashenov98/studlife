from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import CustomUser, Organization
from users.serializers import CustomUserSerializer, OrganizationSerializer
# Create your views here.

class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_serializer_class(self):
        return CustomUserSerializer

class OrganizationAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer